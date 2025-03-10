from pdfminer.high_level import extract_text
import docx2txt
from logger import get_logger

# Setup module logger
logger = get_logger('doc_utils')

def extract_text_from_pdf(file):
    logger.debug(f"Extracting text from PDF file")
    try:
        text = extract_text(file)
        logger.info(f"Successfully extracted {len(text)} characters from PDF")
        return text
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        raise


def extract_text_from_docx(file):
    logger.debug(f"Extracting text from DOCX file")
    try:
        text = docx2txt.process(file)
        logger.info(f"Successfully extracted {len(text)} characters from DOCX")
        return text
    except Exception as e:
        logger.error(f"Error extracting text from DOCX: {str(e)}")
        raise


def extract_text_from_upload(file):
    logger.info(f"Processing uploaded file of type: {file.type}")
    
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
        logger.info("Processing JSON file")
        content = file.getvalue().decode("utf-8")
        logger.debug(f"Successfully extracted {len(content)} characters from JSON")
        return content
    else:
        logger.info(f"Processing text file")
        content = file.getvalue().decode("utf-8")
        logger.debug(f"Successfully extracted {len(content)} characters from text file")
        return content


def escape_for_latex(data):
    """
    Recursively escapes LaTeX special characters in strings within a data structure.
    
    Args:
        data: Input data which can be a dictionary, list, or string
        
    Returns:
        The data with all strings escaped for LaTeX
    """
    logger.debug("Escaping special characters for LaTeX")
    
    if isinstance(data, dict):
        return {k: escape_for_latex(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [escape_for_latex(item) for item in data]
    elif isinstance(data, str):
        # Replace LaTeX special characters with their escaped versions
        for char, replacement in [
            ("\\", "\\textbackslash{}"),
            ("&", "\\&"),
            ("%", "\\%"),
            ("$", "\\$"),
            ("#", "\\#"),
            ("_", "\\_"),
            ("{", "\\{"),
            ("}", "\\}"),
            ("~", "\\textasciitilde{}"),
            ("^", "\\textasciicircum{}"),
        ]:
            data = data.replace(char, replacement)
        return data
    else:
        return data
