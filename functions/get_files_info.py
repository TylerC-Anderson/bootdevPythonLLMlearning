import os
import traceback

def get_files_info(working_directory, directory="."):
    
    try:


        requested_directory = os.path.join(working_directory, directory)
        abs_r_directory = os.path.abspath(requested_directory)

        abs_w_directory = os.path.abspath(working_directory)
        directory_check = os.path.isdir(abs_r_directory)

        if (directory_check == False):
            error = f'Error: "{directory}" is not a directory'
            return error
        
        if ((directory not in os.listdir(abs_w_directory)) and (abs_r_directory!=abs_w_directory)):
            error = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            return error
        
        result_string = ''

        for file in os.listdir(abs_r_directory):
            working_file = os.path.join(abs_r_directory, file)
            result_string+=f"- {file}: file_size={os.path.getsize(working_file)} bytes, is_dir={os.path.isdir(working_file)}\n"
        
        return(result_string)    


    except Exception as e:
        return f'Error: {traceback.format_exc()}'
