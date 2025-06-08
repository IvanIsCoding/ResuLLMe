import streamlit as st
import streamlit_ext as ste
import streamlit_pydantic as sp
import json

from templates import generate_latex, template_commands
from render import render_latex, filter_json_resume

from data_modelling import Resume

if 'saved_json_resume' not in st.session_state:
    st.session_state.saved_json_resume = dict()

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

st.json(st.session_state.saved_json_resume)

template_options = list(template_commands.keys())

chosen_option = st.selectbox(
    "Select a template to use for your resume",
    template_options,
    index=0,  # default to the first option
)

json_resume_from_form = sp.pydantic_input(key="resume_form", model=Resume.parse_obj(st.session_state.saved_json_resume))

st.json(json_resume_from_form)

section_ordering = st.multiselect(
    "Optional: which section ordering would you like to use?",
    ["education", "work", "skills", "projects", "awards"],
    ["education", "work", "skills", "projects", "awards"],
)

generate_button = st.button("Render Resume")

if generate_button:
    json_resume_to_render = filter_json_resume(json_resume_from_form)
    latex_resume = generate_latex(chosen_option, json_resume_to_render, section_ordering)

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
                data=json.dumps(json_resume_to_render, indent=4),
                file_name="resume.json",
                mime="text/json",
            )
    except Exception as e:
        st.error("An error occurred while generating the resume. Please try again.")
        st.write(e)
