import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Security check
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # File checks
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        full_args = ["python", abs_file_path] + args

        completed_process = subprocess.run(
            full_args,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30
        )

        stdout = completed_process.stdout.strip()
        stderr = completed_process.stderr.strip()

        if completed_process.returncode != 0:
            return f"Error: Process exited with code {completed_process.returncode}\nSTDERR:\n{stderr}"

        return f"STDOUT:\n{stdout}" if stdout else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"
