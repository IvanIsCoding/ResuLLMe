# ResuLLMe [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://resullme.streamlit.app/) [![](https://img.shields.io/github/license/IvanIsCoding/ResuLLMe)](https://github.com/IvanIsCoding/ResuLLMe/blob/main/LICENSE) ![](https://img.shields.io/badge/code%20style-black-black)

---

![](./.github/images/Preview.png)

## 🚀 Concept

ResuLLMe is a prototype that uses Large Language Models (LLMs) to tailor résumés. It's goal is to enhance résumés to help candidates avoid common mistakes that occur while applying for jobs. It is like a smart career advisor to check your résumé.

You can use ResuLLMe live at [https://resullme.streamlit.app/](https://resullme.streamlit.app/).

## 🛠 How It Works

ResuLLMe receives your previous CV as a PDF or Word Document. Then, it uses LLMs to:
* Improve the résumé following published résumé guidelines by well-reputed schools
* Convert the résumés to a JSON Resume format
* Render the JSON resume using LaTeX to generate a new PDF of the enhanced resume

## 🏃 Running

To run ResuLLMe locally, the simplest way is to use Docker:

```
docker-compose up -d
```

This will make the app avaialable at [`https://localhost:8501/`](https://localhost:8501/)

### 🪄 Installation Instructions for Running Natively

To run the app without Docker, you will need to install two things for the app to work. The first item is to install the Python dependencies:

```
pip install -r requirements.txt
```

The second item is to install the LaTeX packages:

```
xargs sudo apt install -y < packages.txt
```

Lastly, to run ResuLLMe locally, execute:

```
streamlit run src/Main.py
```

## 🤲 Contributing

ResuLLMe is an open source project.

If you want to contribute, open a [Pull requests](https://github.com/360macky/project-name/pulls). 
All contributions are welcome, but some that would particularly be useful to the community are:
* Fixes in existing LaTeX templates
* Adding new LaTeX templates
* Improved prompts
* Support for other LLMs (e.g. Bard, Claude, LLaMA)
