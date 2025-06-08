import streamlit as st
import streamlit_ext as ste
import os

from doc_utils import extract_text_from_upload
import json

IFRAME = '<iframe src="https://ghbtns.com/github-btn.html?user=IvanIsCoding&repo=ResuLLMe&type=star&count=true&size=large" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>'

st.markdown(
    f"""
    # ResuLLMe {IFRAME}
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "Do you want to regenerate your resume with edited information or with a different template? Simply provide the JSON Resume and we will render it for you"
)

uploaded_file = st.file_uploader("Choose a file", type=["json"])

if uploaded_file is not None:
    # Get the CV data that we need to convert to json
    text = extract_text_from_upload(uploaded_file)

    json_resume = json.loads(text)
    st.session_state.saved_json_resume = json_resume

    st.switch_page("pages/00_Edit_JSON_Resume.py")
