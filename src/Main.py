import streamlit as st
import streamlit_ext as ste
import os

from doc_utils import extract_text_from_upload
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
    #if not os.getenv("OPENAI_API_KEY"):
    #    openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    #else:
    #    openai_api_key = os.getenv("OPENAI_API_KEY")
#
    # Get the Job Post Description
    #job_post_description = st.text_area("Job Post Description", height=200)
#
    #chosen_option = st.selectbox(
    #    "Select a template to use for your resume",
    #    template_options,
    #    index=0,  # default to the first option
    #)
#
    #section_ordering = st.multiselect(
    #    "Optional: which section ordering would you like to use?",
    #    ["education", "work", "skills", "projects", "awards"],
    #    ["education", "work", "skills", "projects", "awards"],
    #)

    generate_button = st.button("Generate Resume")

    if generate_button:
        st.write(f"```{text}```")
