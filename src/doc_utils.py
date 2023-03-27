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
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = extract_text_from_docx(file)
        return text
    elif file.type == "application/json":
        return file.getvalue().decode("utf-8")
    else:
        return file.getvalue().decode("utf-8")