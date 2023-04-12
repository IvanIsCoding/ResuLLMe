<p align="center">
    <a href="https://github.com/IvanIsCoding/GNN-for-Combinatorial-Optimization"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=030A0E&center=true&width=435&lines=Learning+how+to+work+with+LLMs" alt="Typing SVG" /></a>
</p>

## Working with JSON

The biggest challenge to make this whole application work was to make Large Language Models output JSON!

The trick for me was to use this line of prompting:

```
You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

Now consider the following TypeScript Interface for the JSON schema:

interface Basics {
    name: string;
    email: string;
    phone: string;
    website: string;
    address: string;
}

Write the basics section according to the Basic schema. On the response, include only the JSON.
```

It turns out that the model we use understands TypeScript quite well, which gets us good JSONs in general.

## LaTeX Templating

The secret was combining LaTeX with Jinja. [The snippet of code from this slideshow was very helpful](https://tug.org/tug2019/slides/slides-ziegenhagen-python.pdf):

```python
latex_jinja_env = jinja2.Environment(
        block_start_string="\BLOCK{",
        block_end_string="}",
        variable_start_string="\VAR{",
        variable_end_string="}",
        comment_start_string="\#{",
        comment_end_string="}",
        line_statement_prefix="%-",
        line_comment_prefix="%#",
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(dir_path),
    )
```