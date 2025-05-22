import re
# Compila expressões regulares para verificar se uma string é um numero 
# ou um Email válido
IS_VALID_EMAIL = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
IS_NUMBER = re.compile(r'^[0-9]*$')

# Função que verifica se uma String é um email válido
def isValidEmail(string):
    return len(IS_VALID_EMAIL.findall(string)) > 0 

# Função que verifica se uma String é um número
def isNumber(string):
    return len(IS_NUMBER.findall(string)) > 0 

