import os
from google.genai import types 
def schema_get_files_info():
    schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
    return schema_get_files_info
def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        if not os.path.isdir(os.path.abspath(full_path)):
            return f'Error: "{directory}" is not a directory'
        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list {directory} as it is outside the permitted working directory'
        return_string = (
            "Results for current directory"
            if directory == "."
            else f"Results for {directory} directory"
        )
        for element in os.listdir(full_path):
            element_path = os.path.join(os.path.abspath(full_path), element)
            file_size = os.path.getsize(element_path)
            dir_bool = os.path.isdir(element_path)
            return_string += f"\n- {element}: file_size={file_size} bytes, is_dir={dir_bool}"
        return return_string
    except Exception:
        return "Error: Dependency Issue, please try again soon."