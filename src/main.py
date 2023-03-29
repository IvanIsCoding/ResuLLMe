import streamlit as st
from doc_utils import extract_text_from_upload
from templates import generate_latex
from render import render_latex
import json

st.title("ResuLLMe")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt", "json"])

if uploaded_file is not None:
    # Get the CV data that we need to convert to json
    text = extract_text_from_upload(uploaded_file)

    # Get the Job Post Description
    job_post_description = st.text_area("Job Post Description", height=200)

    generate_button = st.button("Generate Resume")

    if generate_button:
        json_resume = json.loads(text)
        latex_resume = generate_latex("template1", json_resume)

        resume_bytes = render_latex(
            ["pdflatex", "-interaction=nonstopmode", "resume.tex"], latex_resume
        )

        try:
            btn = st.download_button(
                label="Download PDF",
                data=resume_bytes,
                file_name="resume.pdf",
                mime="application/pdf",
            )
        except Exception as e:
            st.write(e)

        st.download_button(
            label="Download LaTeX Source",
            data=latex_resume,
            file_name="resume.tex",
            mime="application/x-tex",
        )

        st.download_button(
            label="Download Raw JSON Data for Resume",
            data=text,
            file_name="resume.json",
            mime="text/json",
        )
