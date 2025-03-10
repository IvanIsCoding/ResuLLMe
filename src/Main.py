import streamlit as st
import streamlit_ext as ste
import os
import openai
from logger import get_logger

from doc_utils import extract_text_from_upload
from templates import generate_latex, template_commands
from prompt_engineering import generate_json_resume, tailor_resume
from render import render_latex
import json

# Setup module logger
logger = get_logger('main')

def select_llm_model():
    model_type = st.selectbox(
        "Select the model you want to use:",
        ["OpenAI", "Gemini"],
        index=0
    )
    logger.info(f"User selected LLM model: {model_type}")
    return model_type


def get_llm_model_and_api(model_type):
    logger.debug(f"Getting API configuration for model type: {model_type}")
    if model_type == "OpenAI":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            api_key = st.text_input(
                "Enter your OpenAI API Key: [(click here to obtain a new key if you do not have one)](https://platform.openai.com/account/api-keys)",
                type="password",
            )
            logger.info("User prompted to enter OpenAI API key")
        else:
            logger.info("Using OpenAI API key from environment variables")
            
        api_model = os.getenv("OPENAI_DEFAULT_MODEL") or st.selectbox(
            "Select a model to use for the LLMs (gpt-3.5-turbo is the most well-tested):",
            ["gpt-3.5-turbo", "gpt-4-turbo", "gpt-4o"],
            index=0,
        )
    else:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            api_key = st.text_input(
                "Enter your Gemini API Key: [(contact Gemini support for more details)]",
                type="password",
            )
        api_model = "gemini-1.5-flash"
    return api_key, api_model


def main():
    st.set_page_config(page_title="ResuLLMe", layout="wide", page_icon="📄")
    with st.columns([1, 3, 1])[1]:
        st.title("ResuLLMe 📄")
        st.subheader("Generate professional resumes with AI")
        
    logger.info("ResuLLMe application started")

    model_type = select_llm_model()
    api_key, api_model = get_llm_model_and_api(model_type)

    uploaded_resume = st.file_uploader(
        "Upload your resume (PDF, Word, plain text) or a JSON file from a past session",
        type=["pdf", "docx", "txt", "json"],
    )
    
    if uploaded_resume:
        logger.info(f"Resume uploaded: {uploaded_resume.name} ({uploaded_resume.type})")
        
        resume_text = extract_text_from_upload(uploaded_resume)
        if uploaded_resume.type == "application/json":
            try:
                resume_json = json.loads(resume_text)
                logger.info("Successfully loaded resume from JSON")
            except json.JSONDecodeError:
                logger.error("Failed to parse uploaded JSON file")
                st.error("The uploaded JSON file is not valid.")
                return
        else:
            logger.debug("Generating JSON resume from uploaded document")
            with st.spinner("Generating structured resume from your document..."):
                resume_json = generate_json_resume(resume_text, model_type, api_model, api_key)
                logger.info("Generated structured resume from document")
        
        template = st.selectbox(
            "Select a LaTeX template", list(template_commands.keys())
        )
        logger.info(f"User selected template: {template}")
        
        section_ordering = st.multiselect(
            "Optional: which section ordering would you like to use?",
            ["education", "work", "skills", "projects", "awards"],
            ["education", "work", "skills", "projects", "awards"],
        )

        improve_check = st.checkbox("I want to improve the resume with LLMs", value=False)

        generate_button = st.button("Generate Resume")

        if generate_button:
            logger.info(f"User initiated resume generation with template: {template}")
            with st.spinner("Generating your resume..."):
                try:
                    if improve_check:
                        with st.spinner("Tailoring the resume"):
                            resume_json = tailor_resume(resume_json, api_key, api_model, model_type)

                    latex_code = generate_latex(template, resume_json, section_ordering)
                    logger.debug("LaTeX code generated successfully")
                    
                    pdf_bytes = render_latex(template_commands[template], latex_code)
                    logger.info("PDF rendered successfully")
                    
                    st.success("Your resume has been generated!")

                    col1, col2, col3 = st.columns(3)

                    try:
                        with col1:
                            btn = ste.download_button(
                                label="Download PDF",
                                data=pdf_bytes,
                                file_name="resume.pdf",
                                mime="application/pdf",
                            )
                    except Exception as e:
                        st.write(e)

                    with col2:
                        ste.download_button(
                            label="Download LaTeX Source",
                            data=latex_code,
                            file_name="resume.tex",
                            mime="application/x-tex",
                        )

                    with col3:
                        ste.download_button(
                            label="Download JSON Source",
                            data=json.dumps(resume_json, indent=4),
                            file_name="resume.json",
                            mime="text/json",
                        )
                except openai.RateLimitError as e:
                    st.markdown(
                        "It looks like you do not have OpenAI API credits left. Check [OpenAI's usage webpage for more information](https://platform.openai.com/account/usage)"
                    )
                    st.write(e)
                except openai.NotFoundError as e:
                    st.warning(
                        "It looks like you do not have entered you Credit Card information on OpenAI's site. Buy pre-paid credits to use the API and try again.",
                        icon="💳"
                    )
                    st.write(e)
                except Exception as e:
                    logger.error(f"Error during resume generation: {str(e)}")
                    st.error(f"An error occurred during generation: {str(e)}")
    else:
        st.info("Please upload a file to get started.")


if __name__ == "__main__":
    try:
        main()
        logger.info("Application executed successfully")
    except Exception as e:
        logger.critical(f"Unhandled exception in main application: {str(e)}", exc_info=True)
        st.error(f"An unexpected error occurred: {str(e)}")
