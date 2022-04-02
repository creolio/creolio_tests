import os

def get_path_from_filepath(filepath):
    return os.path.dirname(os.path.realpath(filepath))

def get_files_that_end_with(directory, endsWith):
    result = []

    for file in os.listdir(directory):
        if file.endswith(endsWith):
            filename = os.path.join(directory, file)
            result.append(filename)
    
    return result

