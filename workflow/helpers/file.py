import json

def write_text_to_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

def save_as_json(filename, object):
    with open(filename, 'w', encoding="utf8") as outfile:
        json.dump(object, outfile)
