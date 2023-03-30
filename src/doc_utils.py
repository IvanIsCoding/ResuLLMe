from pdfminer.high_level import extract_text
import docx2txt


def extract_text_from_pdf(file):
    return extract_text(file)


def extract_text_from_docx(file):
    return docx2txt.process(file)


def extract_text_from_upload(file):
    if file.type == "application/pdf":
        text = extract_text_from_pdf(file)
        return text
    elif (
        file.type
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ):
        text = extract_text_from_docx(file)
        return text
    elif file.type == "application/json":
        return file.getvalue().decode("utf-8")
    else:
        return file.getvalue().decode("utf-8")


def escape_for_latex(data):
    if isinstance(data, dict):
        new_data = {}
        for key in data.keys():
            new_data[key] = escape_for_latex(data[key])
        return new_data
    elif isinstance(data, list):
        return [escape_for_latex(item) for item in data]
    elif isinstance(data, str):
        # Adapted from https://stackoverflow.com/q/16259923
        latex_special_chars = {
            "&": r"\&",
            "%": r"\%",
            "$": r"\$",
            "#": r"\#",
            "_": r"\_",
            "{": r"\{",
            "}": r"\}",
            "~": r"\textasciitilde{}",
            "^": r"\^{}",
            "\\": r"\textbackslash{}",
            "\n": "\\newline%\n",
            "-": r"{-}",
            "\xA0": "~",  # Non-breaking space
            "[": r"{[}",
            "]": r"{]}",
        }
        return "".join([latex_special_chars.get(c, c) for c in data])

    return data
