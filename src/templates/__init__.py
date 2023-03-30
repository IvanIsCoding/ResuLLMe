import jinja2
import os

template_commands = {
    "Simple": ["pdflatex", "-interaction=nonstopmode", "resume.tex"],
    "Awesome": ["xelatex", "-interaction=nonstopmode", "resume.tex"],
}


def generate_latex(template_name, json_resume):
    dir_path = os.path.dirname(os.path.realpath(__file__))

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

    return use_template(template_name, latex_jinja_env, json_resume)


def use_template(template_name, jinja_env, json_resume):
    PREFIX = f"{template_name}"
    EXTENSION = "tex.jinja"

    resume_template = jinja_env.get_template(f"{PREFIX}/resume.{EXTENSION}")
    basics_template = jinja_env.get_template(f"{PREFIX}/basics.{EXTENSION}")
    education_template = jinja_env.get_template(f"{PREFIX}/education.{EXTENSION}")
    work_template = jinja_env.get_template(f"{PREFIX}/work.{EXTENSION}")
    skills_template = jinja_env.get_template(f"{PREFIX}/skills.{EXTENSION}")
    projects_template = jinja_env.get_template(f"{PREFIX}/projects.{EXTENSION}")
    awards_template = jinja_env.get_template(f"{PREFIX}/awards.{EXTENSION}")

    sections = []
    if "basics" in json_resume:
        firstName = json_resume["basics"]["name"].split(" ")[0]
        lastName = " ".join(json_resume["basics"]["name"].split(" ")[1:])
        sections.append(basics_template.render(
            firstName = firstName, lastName = lastName, **json_resume["basics"]
        ))
    if "education" in json_resume and len(json_resume["education"]) > 0:
        sections.append(
            education_template.render(
                schools=json_resume["education"], heading="Education"
            )
        )
    if "work" in json_resume and len(json_resume["work"]) > 0:
        sections.append(
            work_template.render(works=json_resume["work"], heading="Work Experience")
        )
    if "skills" in json_resume and len(json_resume["skills"]) > 0:
        sections.append(
            skills_template.render(skills=json_resume["skills"], heading="Skills")
        )
    if "projects" in json_resume and len(json_resume["projects"]) > 0:
        sections.append(
            projects_template.render(
                projects=json_resume["projects"], heading="Projects"
            )
        )
    if "awards" in json_resume and len(json_resume["awards"]) > 0:
        sections.append(
            awards_template.render(awards=json_resume["awards"], heading="Awards")
        )

    resume = resume_template.render(sections=sections)
    return resume
