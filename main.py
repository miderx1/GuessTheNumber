
from styles import setupTheme
from pages import Main_Window
import json

from PySide6.QtWidgets import QApplication
import sys

contas = []

try:
    with open('contas.json','r',encoding='utf8') as arquivo:
        contas = json.load(arquivo)
except:
    pass

app = QApplication(sys.argv)
pages = Main_Window(contas)
setupTheme(app)
pages.show()
app.exec()
pages.saveUserStats()