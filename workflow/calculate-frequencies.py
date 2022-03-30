import os
import re


script_directory = os.path.dirname(os.path.realpath(__file__))

def read_chunks_from_srt(filename):
    result = []
    
    with open(filename) as file:
        chunk = read_chunk(file)

        while chunk != None:
            result.append(chunk)
            chunk = read_chunk(file)

    return result

def read_chunk(file):
    number = file.readline()
    if not (number.strip()):
        return None

    timestamps = file.readline()
    content = ""
    while True:
        line = file.readline()
        line_without_linefeed = line.strip()
        if not line_without_linefeed:
            return {
                "number" : number.strip(),
                "timestamps": timestamps.strip(),
                "content" : content.strip()
            }
        content += line

def get_text_from(filename):
    chunks = read_chunks_from_srt(filename)
    text = ""

    for chunk in chunks:
        text += chunk["content"] + "\n"
    
    return text

def remove_html_from_string(value):
    CLEANR = re.compile('<.*?>') 
    cleantext = re.sub(CLEANR, '', value)
    return cleantext

def split_into_words(text):
    pass

def write_text_to_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

for file in os.listdir(script_directory):
    if file.endswith(".srt"):
        filename = os.path.join(script_directory, file)
        print(f"  - processing {filename} ...")
        text = get_text_from(filename)
        text = remove_html_from_string(text)
        write_text_to_file(filename + ".txt", text)




        
