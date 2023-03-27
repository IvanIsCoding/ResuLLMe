import pypdf
import docx2txt

def extract_text_from_pdf(file):
    text = []

    pdf_reader = pypdf.PdfReader(file)
        
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text.append(page_obj.extract_text())

    return "\n".join(text)

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