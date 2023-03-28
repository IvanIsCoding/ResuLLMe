import streamlit as st
from doc_utils import extract_text_from_upload
from templates import generate_latex
import json

st.title('ResuLLMe')

uploaded_file = st.file_uploader(
    "Choose a file", 
    type=["pdf", "docx", "txt", "json"]
)

if uploaded_file is not None:
    st.write(uploaded_file.type)

    # Get the CV data that we need to convert to json
    text = extract_text_from_upload(uploaded_file)
    st.write(text)

    # Get the Job Post Description
    job_post_description = st.text_area("Job Post Description", height=200)

    generate_button = st.button("Generate Resume")

    if generate_button:

        json_resume = json.loads(text)
        latex_resume = generate_latex('template1', json_resume)
        st.write(f"```\n{latex_resume}\n```")

        #st.download_button(
        #    label="Download Resume",
        #    data=text, # TODO: replace with PDF from LaTeX
        #    file_name='resullme.json',
        #    mime='text/json',
        #)

        #st.download_button(
        #    label="Download Raw Data for Resume",
        #    data=text, # TODO: replace with JSON from GPT-4
        #    file_name='resullme.json',
        #    mime='text/json',
        #)
