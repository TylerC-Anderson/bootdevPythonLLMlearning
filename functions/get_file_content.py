import os
import traceback
import yaml

config_path = os.path.abspath("config.yml")
config = yaml.safe_load(open(config_path))

MAX_CHARS = config["files"]["MAX_CHARS"]

def get_file_content(working_directory, file_path):

    requested_directory = os.path.join(working_directory, file_path)
    abs_r_file = os.path.abspath(requested_directory)

    abs_w_directory = os.path.abspath(working_directory)

    is_file=os.path.isfile(abs_r_file)

    dir_list = os.listdir(abs_w_directory)

    # TODO: fix this check, doesn't check the whole path correctly (pkg/calculator.py returns as outside permitted directory)
    if (not in_allowed_path and requested_directory!=abs_w_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if (not is_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(abs_r_file, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if (os.path.getsize(abs_r_file) > MAX_CHARS):
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return file_content_string