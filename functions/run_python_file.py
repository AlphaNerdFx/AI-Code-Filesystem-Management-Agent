import subprocess
import os
from google.genai import types 
def schema_run_python_file():
    schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run the Python file with the specified arguments in the specified directory, the execution of the python file is constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The python file to execute with the specified arguments is relative to the working directory. If the file provided isn't Python or the file path provided doesn't exist, an error will be displayed.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="The arguments necessary for this python file to be executed. if no arguments are provided, the python file doesn't necessitate any arguments for its execution and an empty list will be provided.",
            ),
        },
    ),
)
    return schema_run_python_file
def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_work_dir = os.path.abspath(working_directory)
        abs_file = os.path.abspath(os.path.join(abs_work_dir, file_path))
        if not abs_file.startswith(abs_work_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file):
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        completed = subprocess.run(
            ["python", abs_file] + args,
            cwd=abs_work_dir,
            timeout=30,
            capture_output=True,
            text=True
        )
        stdout = completed.stdout.strip()
        stderr = completed.stderr.strip()
        output_parts = []
        if stdout:
            output_parts.append(f"STDOUT:\n{stdout}")
        if stderr:
            output_parts.append(f"STERR:\n{stderr}")
        if completed.returncode != 0:
            output_parts.append(f"Process exited with code {completed.returncode}")
        if not output_parts:
            return "No output produced"
        return "\n\n".join(output_parts)
    except Exception as e:
        return f"Error executing Python file: {e}"