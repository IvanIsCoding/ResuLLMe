import streamlit as st

IFRAME = '<iframe src="https://ghbtns.com/github-btn.html?user=IvanIsCoding&repo=ResuLLMe&type=star&count=true&size=large" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>'

st.markdown(
    f"""
    # ResuLLMe's Frequently Asked Questions {IFRAME}
    """,
    unsafe_allow_html=True,
)

with st.expander("**Do I need an OpenAI/Gemini API Key to run ResuLLMe?**"):
    st.markdown(
    """
    **No**, Resullme is able to use any OpenAPI-compatible endpoint, such as [Ollama](https://github.com/ollama/ollama). If you intend on using ChatGPT or Google Gemini, an API key is required.  You can obtain your key [openai](https://platform.openai.com/account/api-keys)/[Gemini](https://aistudio.google.com/ ).
    """
    )

with st.expander("**Can I store my OpenAI/Gemini API Key instead of manually re-entering it?**"):
    st.markdown(
    """
    **Yes**, you can store your key in an environment variable. Use `OPENAI_API_KEY` for openAI, `GEMINI_API_KEY` for Google Gemini, and either for self-hosted. If the environment variable `OPENAI_API_KEY`/`GEMINI_API_KEY` is not defined, ResuLLMe will prompt the user for a key.
    """
    )

with st.expander("**I want to use my own custom format to render my résumé. Is this possible?**"):
    st.markdown(
    """
    Currently, you **cannot** use your own custom format for your résumé.
    """
    )

with st.expander("**What is the LaTeX format?**"):
    st.markdown(
    """
    LaTeX is a document preparation system that is used to render PDFs. ResuLLMe uses LaTeX to render a new AI-curated résumé in a format chosen by you!
    """
    )


with st.expander("**What is the JSON schema for the résumé?**"):
    st.markdown(
    """
    To render the LaTeX file, we use a JSON schema to format data and allow standardized processing. You can look at this [example](https://github.com/IvanIsCoding/ResuLLMe/blob/main/.github/Turing.json) to examine the schema.
    """
    )

with st.expander("**There is information on my résumé that is not accurate. How do I fix it?**"):
    st.markdown(
    """
    Sometimes, LLMs can hallucinate and produce information that is not correct. If this happened to your résumé,
    there are two options to editing it:
        
    * Download the JSON file, and manually edit it using a text editor and render it again by going to [Render JSON Resume](/Render_JSON_Resume).
        
    * Download the LaTeX file and edit it on [Overleaf (or your favorite LaTeX editor)](/Edit_LaTeX_on_Overleaf).    

    """
    )
