import os
from google.genai import types 
def schema_write_file():
    schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write the content provided to the file given in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write content to, relative to the working directory. If no content/working director or file path provided, an error will be displayed.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write, relative to the working directory. If no content/working director or file path provided, an error will be displayed.",
            ),
        },
    ),
)
    return schema_write_file
def write_file(working_directory, file_path, content):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
        if not abs_file_path.startswith(abs_working_directory + os.sep):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        parent_dir = os.path.dirname(abs_file_path)
        os.makedirs(parent_dir, exist_ok=True)
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f"Successfully wrote to \"{file_path}\"({len(content)} characters written)"
    except Exception:
        return "Error: Dependency error, please try again later."
