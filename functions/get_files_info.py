import os
import traceback

def get_files_info(working_directory, directory=None):
    
    try:
        abs_directory = os.path.abspath(directory)
        abs_w_directory = os.path.abspath(working_directory)
        directory_check = os.path.isdir(abs_directory)

        if (abs_directory not in os.listdir(abs_w_directory)):
            error = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            return error
        if (directory_check == False):
            error = f'Error: "{directory}" is not a directory'
            return error
        
        result_string = ''

        for file in os.listdir(abs_directory):
            result_string+=f"- {file}: file_size={os.path.getsize(file)} bytes, is_dir={os.path.isdir(file)}\n"
        
        print(result_string)    


    except Exception as e:
        return f'Error: {traceback.format_exc()}'
