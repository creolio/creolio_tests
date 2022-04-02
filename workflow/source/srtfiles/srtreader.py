from textprocessing import html

def read_all_chunks(filename):
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
                "content" : html.remove_from_string(content.strip())
            }
        content += line

def get_content_as_plain_text(filename):
    chunks = read_all_chunks(filename)
    text = ""

    for chunk in chunks:
        text += chunk["content"] + "\n"
    
    return text