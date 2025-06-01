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
        
        latex_command_conda = [c for c in latex_command]

        if latex_command_conda[0] == "tectonic":
            if "CONDA_PREFIX" in os.environ:
                conda_bin = os.environ["CONDA_PREFIX"] + "/bin"
                latex_command_conda[0] = conda_bin + "/tectonic"
            else:
                import pathlib
                directory = pathlib.Path("/home/adminuser/.conda")
                # Recursively search for files containing 'tectonic' in their name
                for file in directory.rglob("*"):
                    if file.is_file() and "tectonic" in file.name:
                        print(f"DEBUG: {file}")
                raise RuntimeError("Tectonic is NOT running in a conda environment!")
            

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
