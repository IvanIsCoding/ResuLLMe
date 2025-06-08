import streamlit as st
import streamlit_ext as ste
import os
import openai

from doc_utils import extract_text_from_upload
from prompt_engineering import generate_json_resume, tailor_resume


def select_llm_model():
    model_type = st.selectbox(
        "Select the model you want to use:",
        ["OpenAI", "Gemini", "Self-Hosted"],
        index=0,
    )
    return model_type


def get_llm_model_and_api(model_type):
    if model_type == "OpenAI":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            api_key = st.text_input(
                "Enter your OpenAI API Key: [(click here to obtain a new key if you do not have one)](https://platform.openai.com/account/api-keys)",
                type="password",
            )
        api_model = os.getenv("OPENAI_DEFAULT_MODEL") or st.selectbox(
            "Select a model to use for the LLMs (gpt-4.1 is the latest, gpt-3.5-turbo is the most well-tested):",
            ["gpt-4.1-2025-04-14", "gpt-3.5-turbo", "gpt-4-turbo", "gpt-4o"],
            index=0,
        )
    elif model_type == "Gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            api_key = st.text_input(
                "Enter your Gemini API Key: [(contact Gemini support for more details)]",
                type="password",
            )
        api_model = "gemini-2.0-flash"
    else:
        if os.getenv("GEMINI_API_KEY"):
            api_key = os.getenv("GEMINI_API_KEY")
        elif os.getenv("OPENAI_API_KEY"):
            api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            api_key = st.text_input(
                "Enter the self-hosted API key: [(Most times you can just write random text)]",
                type="password",
            )
        # Use Ollama API as default
        location = "http://127.0.0.1:11434/v1"
        location = st.text_input(
            "Enter the self-hosted API location (e.g. " + location + "):",
            type="default",
        )
        model_list = []
        try:
            client = openai.OpenAI(base_url=location, api_key=api_key)
            model_list = [model.id for model in client.models.list()]
        except:
            st.markdown(
                "The current API key or location is incorrect. Please try again."
            )
        api_model = st.selectbox(
            "Select a model to use for the LLMs:", model_list, index=0
        )
    return api_key, api_model


if __name__ == "__main__":
    IFRAME = '<iframe src="https://ghbtns.com/github-btn.html?user=IvanIsCoding&repo=ResuLLMe&type=star&count=true&size=large" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>'

    st.set_page_config(
        page_title="ResuLLMe",
        page_icon=":clipboard:",
        layout="wide",
        initial_sidebar_state="auto",
    )

    st.markdown(
        f"""
        # ResuLLMe {IFRAME}
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "ResuLLMe was updated to v3. If you'd like to use the previous version, see [Legacy ResuLLMe](/Legacy_ResuLLMe)",
        icon="ℹ️",
    )

    st.markdown(
        "Welcome to ResuLLMe! Drop your previous CV below, select one of the templates, and let the LLMs generate your resume for you"
    )

    uploaded_file = st.file_uploader(
        "Choose a file", type=["pdf", "docx", "txt", "json"]
    )

    if uploaded_file is not None:
        # Get the CV data that we need to convert to json
        text = extract_text_from_upload(uploaded_file)

        if len(text) < 50:
            st.warning(
                "The text extracted from the uploaded file is too short. Are you sure this is the correct file?",
                icon="⚠️",
            )

        model_type = select_llm_model()
        api_key, api_model = get_llm_model_and_api(model_type)

        improve_check = st.checkbox(
            "I want to improve the resume with LLMs", value=False
        )

        generate_button = st.button("Generate Resume")

        if generate_button:
            try:
                if improve_check:
                    with st.spinner("Tailoring the resume"):
                        text = tailor_resume(text, api_key, api_model, model_type)

                json_resume = generate_json_resume(text, api_key, api_model, model_type)

                st.session_state.saved_json_resume = json_resume
                st.switch_page("pages/00_Edit_JSON_Resume.py")

            except openai.RateLimitError as e:
                st.markdown(
                    "It looks like you do not have OpenAI API credits left. Check [OpenAI's usage webpage for more information](https://platform.openai.com/account/usage)"
                )
                st.write(e)
            except openai.NotFoundError as e:
                st.warning(
                    "It looks like you do not have entered you Credit Card information on OpenAI's site. Buy pre-paid credits to use the API and try again.",
                    icon="💳",
                )
                st.write(e)
            except Exception as e:
                st.error(
                    "An error occurred while generating the resume. Please try again."
                )
                st.write(e)
    else:
        st.info("Please upload a file to get started.")
