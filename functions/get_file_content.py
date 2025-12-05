import os
from google.genai import types 
def schema_get_file_content():
    schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Display content of a file in the specified directory, constrained to the working directory and an output with a maximum of 10000 characters .",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to display the content of a file from, relative to the working directory. If not provided, an error will be displayed.",
            ),
        },
    ),
)
    return schema_get_file_content
def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_full_path = os.path.abspath(full_path)
        abs_working_dir = os.path.abspath(working_directory)
        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot read {file_path} as it is outside the permitted working directory'
        if not os.path.isfile(abs_full_path):
            return f'Error: File not found or is not a regular file: {file_path}'
        with open(abs_full_path, "r") as f:
            content = f.read(10000)
            if os.path.getsize(abs_full_path) > 10000:
                return content + f"...File \"{file_path}\" truncated at 10000 characters"
            return content
    except Exception:
        return "Dependency error, please try again later."