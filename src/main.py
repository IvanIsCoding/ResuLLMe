import streamlit as st
import streamlit_ext as ste
import os

from doc_utils import extract_text_from_upload, escape_for_latex
from templates import generate_latex, template_commands
from render import render_latex
import json

st.title("ResuLLMe")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt", "json"])

template_options = list(template_commands.keys())

if uploaded_file is not None:
    # Get the CV data that we need to convert to json
    text = extract_text_from_upload(uploaded_file)

    # If not in the environment variables, we ask for the OpenAI API Key
    if not os.getenv("OPENAI_API_KEY"):
        openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    else:
        openai_api_key = os.getenv("OPENAI_API_KEY")

    # Get the Job Post Description
    job_post_description = st.text_area("Job Post Description", height=200)

    chosen_option = st.selectbox(
        "Select a template to use for your resume",
        template_options,
        index=0,  # default to the first option
    )

    section_ordering = st.multiselect(
        "Optional: which section ordering would you like to use?",
        ["education", "work", "skills", "projects", "awards"],
        ["education", "work", "skills", "projects", "awards"],
    )

    generate_button = st.button("Generate Resume")

    if generate_button:
        json_resume = json.loads(text)
        escaped_json_resume = escape_for_latex(json_resume)
        latex_resume = generate_latex(
            chosen_option, escaped_json_resume, section_ordering
        )

        resume_bytes = render_latex(template_commands[chosen_option], latex_resume)

        col1, col2, col3 = st.columns(3)

        try:
            with col1:
                btn = ste.download_button(
                    label="Download PDF",
                    data=resume_bytes,
                    file_name="resume.pdf",
                    mime="application/pdf",
                )
        except Exception as e:
            st.write(e)

        with col2:
            ste.download_button(
                label="Download LaTeX Source",
                data=latex_resume,
                file_name="resume.tex",
                mime="application/x-tex",
            )

        with col3:
            ste.download_button(
                label="Download JSON Source",
                data=text,
                file_name="resume.json",
                mime="text/json",
            )
