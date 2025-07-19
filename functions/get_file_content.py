import os
from config import CONTENT_CHARACTER_LIMIT


def get_file_content(working_directory, file_path):
        file_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs = os.path.abspath(working_directory)

        if not file_path.startswith(working_directory_abs):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if is not a file
        if not os.path.isfile(file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read file
        file_content_string = ""
        try:
             with open(file_path, "r") as f:
                full_content = f.read()
                if len(full_content) > CONTENT_CHARACTER_LIMIT:
                    truncated = full_content[:CONTENT_CHARACTER_LIMIT]
                    truncated += f'\n[...File "{file_path}" truncated at {CONTENT_CHARACTER_LIMIT} characters]'
                    file_content_string = truncated
                else:
                    file_content_string = full_content
        except Exception as e:
            return f"Error: {str(e)}"
        
        return file_content_string
