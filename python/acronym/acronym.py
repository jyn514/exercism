import re

def abbreviate(text):
    regex = re.compile(r'\b\w|(?<=-)')
    # first letter of a word or first letter after a `-`
    return "".join([x.upper() for x in regex.findall(text)])
