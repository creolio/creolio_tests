import re

def remove_from_string(value):
    htmltags_regex = re.compile('<.*?>') 
    cleantext = re.sub(htmltags_regex, '', value)
    return cleantext