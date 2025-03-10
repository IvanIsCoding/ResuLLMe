import tempfile
import subprocess
import os
import shutil
from logger import get_logger

# Setup module logger
logger = get_logger('render')

def render_latex(latex_command, latex_data):
    """
    Render LaTeX data to PDF.
    
    Args:
        latex_command: The LaTeX command to run
        latex_data: The LaTeX document content
        
    Returns:
        The binary PDF data
    """
    logger.info("Starting LaTeX rendering process")
    logger.debug(f"LaTeX data length: {len(latex_data)} characters")
    
    src_path = os.path.dirname(os.path.realpath(__file__)) + "/inputs"
    logger.debug(f"Source path for auxiliary files: {src_path}")

    try:
        with tempfile.TemporaryDirectory() as tmpdirname:
            logger.debug(f"Created temporary directory: {tmpdirname}")
            
            # Copy auxiliary files to temporary directory
            shutil.copytree(src_path, tmpdirname, dirs_exist_ok=True)
            logger.debug("Copied auxiliary files to temporary directory")

            # write latex data to a file
            with open(f"{tmpdirname}/resume.tex", "w") as f:
                f.write(latex_data)
            logger.debug("Wrote LaTeX data to temporary file")

            # run latex command
            logger.info(f"Running LaTeX command: {latex_command}")
            latex_process = subprocess.Popen(
                latex_command, 
                cwd=tmpdirname,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = latex_process.communicate()
            exit_code = latex_process.wait()
            
            if exit_code != 0:
                logger.error(f"LaTeX rendering failed with exit code {exit_code}")
                logger.debug(f"LaTeX stderr: {stderr.decode('utf-8', errors='ignore')}")
                raise RuntimeError(f"LaTeX rendering failed with exit code {exit_code}")
            else:
                logger.info("LaTeX rendering completed successfully")
                
            # Check if PDF was created
            pdf_path = f"{tmpdirname}/resume.pdf"
            if not os.path.exists(pdf_path):
                logger.error(f"LaTeX process completed but PDF was not created at {pdf_path}")
                logger.debug(f"LaTeX stdout: {stdout.decode('utf-8', errors='ignore')}")
                logger.debug(f"LaTeX stderr: {stderr.decode('utf-8', errors='ignore')}")
                raise FileNotFoundError(f"PDF file was not created at {pdf_path}")
                
            # read pdf data
            with open(pdf_path, "rb") as f:
                pdf_data = f.read()
            
            pdf_size = len(pdf_data)
            logger.info(f"PDF generated successfully, size: {pdf_size} bytes")
            
        return pdf_data
        
    except Exception as e:
        logger.error(f"Error during LaTeX rendering: {str(e)}", exc_info=True)
        raise
