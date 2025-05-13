import re

IS_VALID_EMAIL = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def isValidEmail(string):
    return len(IS_VALID_EMAIL.findall(string)) > 0 
