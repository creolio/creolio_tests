import json
import os
import re
import split_fr as split_fr

script_directory = os.path.dirname(os.path.realpath(__file__))

def read_chunks_from_srt(filename):
    result = []
    
    with open(filename, encoding="utf8") as file:
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

def write_text_to_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

def calculate_frequencies(words):
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    result = dict(sorted(result.items(), key=lambda item: item[1], reverse = True))

    return result

def save_json(filename, object):
    with open(filename, 'w', encoding="utf8") as outfile:
        json.dump(object, outfile)

def process_srts_in_folder(folder):
    for file in os.listdir(folder):
        if file.endswith(".srt"):
            filename = os.path.join(folder, file)
            print(f"  - processing {filename} ...")
            
            text = get_text_from(filename)
            text = remove_html_from_string(text)
            write_text_to_file(filename + ".txt", text)

            if filename.endswith("_fr.srt"):
                words = split_fr.split_into_words(text)
                save_json(filename + ".json", calculate_frequencies(words))

process_srts_in_folder(script_directory)


        
