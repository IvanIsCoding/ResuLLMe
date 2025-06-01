import tempfile
import subprocess
import os
import shutil
import pathlib
import sys
import functools

@functools.lru_cache(maxsize=None)
def find_tectonic_streamlit_cloud():
    import streamlit as st
    current_dir = pathlib.Path(st.__file__).parent
    while current_dir.parent != current_dir:
        if (current_dir / "tectonic").exists():
            return str(current_dir / "tectonic")
        if (current_dir / "bin").exists():
            current_bin_dir = current_dir / "bin"
            if (current_bin_dir / "tectonic").exists():
                return str(current_bin_dir / "tectonic")
        current_dir = current_dir.parent
    return "tectonic"

def render_latex(latex_command, latex_data):
    src_path = os.path.dirname(os.path.realpath(__file__)) + "/inputs"

    with tempfile.TemporaryDirectory() as tmpdirname:
        # Copy auxiliary files to temporary directory
        shutil.copytree(src_path, tmpdirname, dirs_exist_ok=True)

        # write latex data to a file
        with open(f"{tmpdirname}/resume.tex", "w") as f:
            f.write(latex_data)
        
        latex_command_conda = [c for c in latex_command]

        if "IS_STREAMLIT_CLOUD" in os.environ:
            tectonic_path = find_tectonic_streamlit_cloud()
            print(f"DEBUG: Running in Streamlit Cloud, Tectonic path: {tectonic_path}")
            latex_command_conda = [tectonic_path] + [c for c in latex_command][1:]
            

        # Find the Tectonic Vendored Cache
        current_dir = pathlib.Path(__file__).resolve().parent
        cache_dir = current_dir.parents[1] / "tectonic_cache"

        # Inject Tectonic Environment Variables
        tectonic_env = os.environ.copy()
        tectonic_env["XDG_CACHE_HOME"] = str(cache_dir)
        tectonic_env["TECTONIC_CACHE_DIR"] = f"{str(cache_dir)}/tectonic_cache"

        # run latex command
        latex_process = subprocess.Popen(
            latex_command_conda, cwd=tmpdirname, env=tectonic_env,
        )
        latex_process.wait()

        # read pdf data
        with open(f"{tmpdirname}/resume.pdf", "rb") as f:
            pdf_data = f.read()

    return pdf_data
