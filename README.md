# ResuLLMe [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://resullme.streamlit.app/)

ResuLLMe is live at [https://resullme.streamlit.app/](https://resullme.streamlit.app/). As of now, you need an OpenAI API token for the application to work.

## 🚀 Concept

ResuLLMe is a prototype that uses Large Language Models (LLMs) to tailor resumes. Its goal is to enhance resumes to help candidates avoid commonplace mistakes that happen when sending resumes to job posts. It is like a smart career advisor to check your resume.

## 🛠 How It Works

ResuLLMe receives your previous CV in PDF, Docx, our text format. Then, it uses LLMs to:
* Improve the resume following published resume guidelines by well-reputed schools
* Conver the resume to a JSON Resume format
* Render the JSON resume using LaTeX to generate a new PDF of the enhanced resume

## 🏃 Running

To run ResuLLMe, execute:

```
streamlit run src/Main.py
```

Notice that you will need to install the dependencies in `requirements.txt` for your code to work, and install the packages in `packages.txt` for the LaTeX rendering to work (or equivalent if not using Ubuntu). 