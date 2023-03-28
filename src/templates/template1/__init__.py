def template1(jinja_env, json_resume):
    PREFIX = "template1"
    EXTENSION = "tex.jinja"
    resume_template = jinja_env.get_template(f"{PREFIX}/resume.{EXTENSION}")
    basics_template = jinja_env.get_template(f"{PREFIX}/basics.{EXTENSION}")

    sections = []
    sections.append(
        basics_template.render(**json_resume["basics"])
    )

    resume = resume_template.render(sections=sections)
    return resume
