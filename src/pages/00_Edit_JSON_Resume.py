import streamlit as st
import streamlit_ext as ste
import streamlit_pydantic as sp
import json

from templates import generate_latex, template_commands
from render import render_latex

from data_modelling import Resume

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

template_options = list(template_commands.keys())

chosen_option = st.selectbox(
    "Select a template to use for your resume",
    template_options,
    index=0,  # default to the first option
)

json_resume = sp.pydantic_input(key="my_form", model=Resume)

st.json(json_resume)

section_ordering = st.multiselect(
    "Optional: which section ordering would you like to use?",
    ["education", "work", "skills", "projects", "awards"],
    ["education", "work", "skills", "projects", "awards"],
)

generate_button = st.button("Generate Resume")

if generate_button:
    latex_resume = generate_latex(chosen_option, json_resume, section_ordering)

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
                data=json.dumps(json_resume, indent=4),
                file_name="resume.json",
                mime="text/json",
            )
    except Exception as e:
        st.error("An error occurred while generating the resume. Please try again.")
        st.write(e)
