import tempfile
import subprocess
import os
import shutil
import pathlib


def render_latex(latex_command, latex_data):
    src_path = os.path.dirname(os.path.realpath(__file__)) + "/inputs"

    with tempfile.TemporaryDirectory() as tmpdirname:
        # Copy auxiliary files to temporary directory
        shutil.copytree(src_path, tmpdirname, dirs_exist_ok=True)

        # write latex data to a file
        with open(f"{tmpdirname}/resume.tex", "w") as f:
            f.write(latex_data)

        # Find the Tectonic Vendored Cache
        current_dir = pathlib.Path(__file__).resolve().parent
        cache_dir = current_dir.parents[1] / "tectonic_cache"

        # Inject Tectonic Environment Variables
        tectonic_env = os.environ.copy()
        tectonic_env["XDG_CACHE_HOME"] = str(cache_dir)
        tectonic_env["TECTONIC_CACHE_DIR"] = f"{str(cache_dir)}/tectonic_cache"
        print(f"DEBUG: Using this environment: {tectonic_env}")

        # run latex command
        latex_process = subprocess.Popen(
            latex_command, cwd=tmpdirname, env=tectonic_env,
        )
        latex_process.wait()

        # read pdf data
        with open(f"{tmpdirname}/resume.pdf", "rb") as f:
            pdf_data = f.read()

    return pdf_data
