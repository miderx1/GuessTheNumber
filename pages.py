from pageUi import Ui_StackedWidget
from styles import PRIMARY_COLOR, DARKEST_PRIMARY_COLOR
from utils import isValidEmail
from PySide6.QtWidgets import QStackedWidget
import json


def make_slot(func,*args,**kwargs):
    def inner_func():
        func(*args,**kwargs)
    return inner_func

class Main_Window(Ui_StackedWidget,QStackedWidget):
    def __init__(self,accounts:list, parent=None, ):
        super().__init__(parent)
        self.setupUi(self)
        self.accounts = accounts
        self._activeAccount = {}
        self._shots = 0

        self.buttonLogin.setProperty('cssClass','specialButton')
        self.inputUser.setProperty('cssClass','logPageInput')
        self.inputPassword.setProperty('cssClass','logPageInput')
        self.labelUser.setProperty('cssClass','logPageLabel')
        self.labelPassword.setProperty('cssClass','logPageLabel')
        self.labelTitle.setProperty('cssClass','title')
        self.buttonRegister.setProperty('cssClass','secondButton')
        self.forgetPassLabel.setProperty('cssClass','secondButton')
        self.labelInfo.setProperty('cssClass','warning')

        self.cadasterTitle.setProperty('cssClass','title')
        self.cadEmailInput.setProperty('cssClass','logPageInput')
        self.cadPasswordInput.setProperty('cssClass','logPageInput')
        self.cadUserInput.setProperty('cssClass','logPageInput')
        self.cadConfPassInput.setProperty('cssClass','logPageInput')
        self.backToLoginButton.setProperty('cssClass','secondButton')
        self.registerButton.setProperty('cssClass','specialButton')
        self.cadConfPassLabel.setProperty('cssClass','logPageLabel')
        self.cadPasswordLabel.setProperty('cssClass','logPageLabel')
        self.cadUserLabel.setProperty('cssClass','logPageLabel')
        self.cadEmailLabel.setProperty('cssClass','logPageLabel')

        self.playButton.setProperty('cssClass','specialButton')
        self.logoutButton.setProperty('cssClass','secondButton')
        self.menuTitle.setProperty('cssClass','title')
        self.menuTitle.setStyleSheet('font-size: 30px')
        self.winsLabel.setProperty('cssClass','logPageLabel')
        self.winsLabel.setStyleSheet('color: green')
        self.lossLabel.setStyleSheet('color: red')
        self.lossLabel.setProperty('cssClass','logPageLabel')
        self.usernameLabel.setProperty('cssClass','logPageLabel')

        self.easyButton.setProperty('cssClass','specialButton')
        self.mediumButton.setProperty('cssClass','specialButton')
        self.hardButton.setProperty('cssClass','specialButton')
        self.answerButton.setProperty('cssClass','specialButton')
        self.backToMenuButton.setProperty('cssClass','secondButton')

        self.buttonRegister.clicked.connect(lambda: self.setCurrentWidget(self.registerPage))
        self.backToLoginButton.clicked.connect(lambda: self.setCurrentWidget(self.loginPage))
        self.logoutButton.clicked.connect(self.saveAndBack)
        self.buttonLogin.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)
        self.playButton.clicked.connect(self.startGame)
        self.answerButton.setDisabled(True)
    
    def saveAndBack(self):
        self.saveUserStats()
        self.setCurrentWidget(self.loginPage)
    
    def startGame(self):
        shots = 10
        self.setCurrentWidget(self.gamePage)
        self.shotsLabel.setText(f'Tentativas restantes: {shots}')


    def saveUserStats(self):
        try:
            with open('contas.json', 'w', encoding='utf8') as file:
                json.dump(self.accounts,file,ensure_ascii=True,indent=2)
        except:
            print('Falha ao tentar realizar Backup')

    def mainPageUpdate(self):
        self.winsLabel.setText(f'Vitórias: {self._activeAccount['win']}')
        self.lossLabel.setText(f'Derrotas: {self._activeAccount['loss']}')
        self.setCurrentWidget(self.mainPage)  

    def login(self):
        user = self.inputUser.text()
        password = self.inputPassword.text()
        print('procurando usuário', user,password)
        for i in self.accounts:
            if i['login'] == user:
                
                if i['senha'] == password:

                    self._activeAccount = i
                    self.usernameLabel.setText(user.upper())
                    self.mainPageUpdate()
                    self.labelInfo.clear()
                    return
                
                self.labelInfo.setText('Senha incorreta')
                return
        
        self.labelInfo.setText('Usuário não encontrado')
    def register(self):

        self.cadUserInfo.clear()
        self.cadPassInfo.clear()
        self.cadEmailInfo.clear()
        self.cadConfPassInfo.clear()

        user = self.cadUserInput.text()
        password = self.cadPasswordInput.text()
        email = self.cadEmailInput.text()
        confPassword = self.cadConfPassInput.text()

        print('Registrando usuário',user,password,email,confPassword)
               
        if not user:
            self.cadUserInfo.setText('Preencha esse campo')
            return
        
        for i in self.accounts:
            if user == i['login']:
                self.cadUserInfo.setText('Usuário já cadastrado')
                return
            if email == i['email']:
                self.cadEmailInfo.setText('Email já cadastrado')
                return
        if not email:
            self.cadEmailInfo.setText('Preencha esse campo')
            return
        elif not isValidEmail(email):
            self.cadEmailInfo.setText('Email inválido')
            return
        
        if not password:
            self.cadPassInfo.setText('Preencha esse campo')
            return
        
        if password != confPassword:
            self.cadConfPassInfo.setText('Senhas não conferem')
            return

        activeUser = dict(
            login = user,
            senha = password,
            email = email,
            win = 0,
            loss = 0,
        )
        self._activeAccount = activeUser
        self.accounts.append(self._activeAccount)
        self.setCurrentWidget(self.mainPage)
        self.usernameLabel.setText(user)
        self.mainPageUpdate()

        
