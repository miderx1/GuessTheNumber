from pageUi import Ui_StackedWidget
from styles import PRIMARY_COLOR, DARKEST_PRIMARY_COLOR
from utils import isValidEmail
from PySide6.QtWidgets import QStackedWidget,QPushButton
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

        self.labelTitle.setProperty('cssClass','title')
        self.buttonRegister.setProperty('cssClass','specialButton')
        self.forgetPassLabel.setProperty('cssClass','specialButton')
        self.labelInfo.setProperty('cssClass','warning')
        self.cadasterTitle.setProperty('cssClass','title')

        self.cadConfPassInfo.setProperty('cssClass','warning')
        self.cadEmailInfo.setProperty('cssClass','warning')
        self.cadUserInfo.setProperty('cssClass','warning')
        self.cadPassInfo.setProperty('cssClass','warning')
        self.backToLoginButton.setProperty('cssClass','specialButton')

        self.logoutButton.setProperty('cssClass','specialButton')
        self.menuTitle.setProperty('cssClass','title')
        self.menuTitle.setStyleSheet('font-size: 30px')
        self.winsLabel.setStyleSheet('color: green')
        self.lossLabel.setStyleSheet('color: red')

        self.gameTitle.setProperty('cssClass','title')

        self.buttonRegister.clicked.connect(lambda: self.setCurrentWidget(self.registerPage))
        self.backToLoginButton.clicked.connect(lambda: self.setCurrentWidget(self.loginPage))
        self.logoutButton.clicked.connect(self.saveAndBack)
        self.buttonLogin.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)
        self.playButton.clicked.connect(self.startGame)


        # easyPlay = make_slot(self.play,self.easyButton)
        # mediumPlay = make_slot(self.play,self.mediumButton)
        # hardPlay = make_slot(self.play,self.hardButton)

        self.easyButton.clicked.connect(self.play)
        self.mediumButton.clicked.connect(self.play)
        self.hardButton.clicked.connect(self.play)

        self.setGameVisible(False)
        


    def play(self):
        button = self.sender()

        dificultButtons = [self.easyButton,self.mediumButton,self.hardButton]

        dificults = {
            'Fácil' : 100,
            'Médio' : 150,
            'Difícil' : 200
        }

        for i in dificultButtons:
            if button.text() == i.text():
                gameRange = dificults[button.text()]
                button.setStyleSheet(f'background-color: {DARKEST_PRIMARY_COLOR}')
            else:
                i.setDisabled(True)
        
        self.rangeLabel.setText(f'Intervalo: 1 até {gameRange}')
        self.setGameVisible(True)
                  

    def setGameVisible(self,value):
        self.shotInput.setVisible(value)
        self.shotsLabel.setVisible(value)
        self.answerButton.setVisible(value)
        self.rangeLabel.setVisible(value)
        self.gameInfoLabel.setVisible(value)

    def saveAndBack(self):
        self.saveUserStats()
        self.setCurrentWidget(self.loginPage)
    
    def startGame(self):
        shots = 10
        self.setCurrentWidget(self.gamePage)
        self.initLabel.setText('Escolha uma dificuldade')


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

        
