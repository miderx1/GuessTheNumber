
from styles import setupLightTheme
from pages import Main_Window
import json

from PySide6.QtWidgets import QApplication
import sys

# Criação da variável que vai receber todas contas cadastradas
accounts = []


# Tenta abrir o arquivo de contas. Caso consiga, manda as contas para a variável accounts
# Caso não consiga, seguirá normalmente, assumindo que não existem contas cadastradas
try:
    with open('contas.json','r',encoding='utf8') as file:
        accounts = json.load(file)
except:
    pass

# Criação do app e de suas paginas
app = QApplication(sys.argv)
pages = Main_Window(accounts)
setupLightTheme(app)
pages.show()
app.exec()

# Salva os dados da conta antes de finalizar o programa
pages.saveUserStats()