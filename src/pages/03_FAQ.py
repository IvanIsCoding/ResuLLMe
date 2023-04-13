import streamlit as st

IFRAME = '<iframe src="https://ghbtns.com/github-btn.html?user=IvanIsCoding&repo=ResuLLMe&type=star&count=true&size=large" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>'

st.markdown(
    f"""
    # ResuLLMe's Frequently Asked Questions {IFRAME}
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """

## There is information on my resume that is not accurate. How do I fix it?

Sometimes, LLMs can hallucinate and produce information that is not correct. If this happend to your resume,
there are two options to editing it:
* Download the JSON file, manually edit it using a text editor and [render it again by going to Render JSON Resume](/Render_JSON_Resume)
* Download the LaTeX file [and edit it on Overleaf (or your favorite LaTeX editor)](/Edit_LaTeX_on_Overleaf)

## What is the JSON schema for the Resume?

We follow a subset of the JSON Resume Schema. You can look at [Alan Turing's JSON Resume for an example of the schema](https://github.com/IvanIsCoding/ResuLLMe/blob/main/.github/Turing.json).

## Is an OpenAI API Key requried to run the application?

As of now, the only LLM we support is ChatGPT. Hence, an OpenAI API Key is required. 
You can get one at [OpenAI's website](https://platform.openai.com/account/api-keys).

If the environment variable `OPENAI_API_KEY` is not defined, ResuLLMe will prompt the user for a key.
Otherwise, it will use the key defined in the environment variable. 

"""
)
