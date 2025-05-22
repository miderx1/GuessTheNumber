from pageUi import Ui_StackedWidget
from styles import PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,DARKER_PRIMARY_COLOR
from utils import isValidEmail, isNumber
from emailSender import sendEmail
from PySide6.QtWidgets import QStackedWidget,QPushButton
import json
import random


def make_slot(func,*args,**kwargs):
    def inner_func():
        func(*args,**kwargs)
    return inner_func

class Main_Window(Ui_StackedWidget,QStackedWidget):
    def __init__(self,accounts:list, parent=None, ):
        super().__init__(parent)
        self.setupUi(self)
        self._accounts = accounts
        self._activeAccount = {}
        self._shots = 0
        self._randomNumber = 0
        self._gameRange = 0

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
        self.passRecInfo.setStyleSheet('font-size: 15px')

        self.gameTitle.setProperty('cssClass','title')
        self.passRecTitle.setProperty('cssClass','title')
        self.backToLoginButton2.setProperty('cssClass','specialButton')

        self.buttonRegister.clicked.connect(lambda: self.setCurrentWidget(self.registerPage))
        self.forgetPassLabel.clicked.connect(lambda: self.setCurrentWidget(self.passRecPage))
        self.backToLoginButton.clicked.connect(lambda: self.setCurrentWidget(self.loginPage))
        self.backToMenuButton.clicked.connect(lambda: self.setCurrentWidget(self.mainPage))
        self.backToLoginButton2.clicked.connect(self.backToLoginPage)

        self.logoutButton.clicked.connect(self.saveAndBack)
        self.buttonLogin.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)
        self.playButton.clicked.connect(self.startGame)
        self.answerButton.clicked.connect(self.sendAnswer)

        self.easyButton.clicked.connect(self.play)
        self.mediumButton.clicked.connect(self.play)
        self.hardButton.clicked.connect(self.play)
        
        self.sendEmailButton.clicked.connect(self.recoverPassword)

    def backToLoginPage(self):
        self.passRecInfo.clear()
        self.emailOrNickInput.clear()
        self.setCurrentWidget(self.loginPage)

    def play(self):
        self.backToMenuButton.setDisabled(True)
        self._shots = 10
        button = self.sender()
        self.gameInfoLabel.clear()
        self.gameInfoLabel.setStyleSheet(f'color: {DARKEST_PRIMARY_COLOR}')

        dificultButtons = [self.easyButton,self.mediumButton,self.hardButton]

        dificults = {
            'Fácil' : 100,
            'Médio' : 150,
            'Difícil' : 200
        }

        for i in dificultButtons:
            if button.text() == i.text():
                self._gameRange = dificults[button.text()]
                button.setStyleSheet(f'background-color: {DARKEST_PRIMARY_COLOR}')

            i.setDisabled(True)

        self._randomNumber = random.randint(1,self._gameRange)
        self.initLabel.setText('Numero sorteado')

        self.rangeLabel.setText(f'Intervalo: 1 até {self._gameRange}')
        self.setGameVisible(True)
        self.shotsLabel.setText(f'Tentativas restantes: {self._shots}')

    def sendAnswer(self):
        answer = self.answerInput.text()
        self.answerInput.clear()

        try:
            smallerOrBigger = 'maior' if int(answer) < self._randomNumber else 'menor'
        except ValueError:
            self.gameInfoLabel.setText('Numero inválido')
            return

        if answer == '696': 
            self.gameInfoLabel.setText(f'Trapaça Ativada! Você ganhou 100 tentativas')
            self._shots += 100
            self.shotsLabel.setText(f'Tentativas restantes: {self._shots}')
            return
        elif answer == '8911': 
            self.gameInfoLabel.setText(f'Trapaça Ativada! sobrou 1 tentativa')
            self._shots = 1
            self.shotsLabel.setText(f'Tentativas restantes: {self._shots}')
            return
        elif answer == '666': 
            ...

        elif int(answer) > self._gameRange or int(answer) < 0:
            self.gameInfoLabel.setText('Numero fora do intervalo')
            return
        
        elif int(answer) > self._randomNumber or int(answer) < self._randomNumber:
            self._shots -= 1

            if self._shots > 1 :
                self.gameInfoLabel.setText(f'Errou! o numero sorteado é {smallerOrBigger} que {answer}')
                self.shotsLabel.setText(f'Tentativas restantes: {self._shots}')
                return

            self.gameInfoLabel.setStyleSheet('color: red')
            self.gameInfoLabel.setText(f'Você perdeu! Tentativas esgotadas.')
            self._activeAccount['loss'] += 1
            self.lossLabel.setText(f'Derrotas: {self._activeAccount['loss']}')
            self.shotsLabel.setText(f'Tentativas restantes: {self._shots}')
            self.backToMenuButton.setDisabled(False)
            self.startGame()
            return
        
        self.gameInfoLabel.setStyleSheet('color: green')
        self.gameInfoLabel.setText(f'Você acertou! o numero sorteado era {answer}')
        self._activeAccount['win'] += 1
        self.winsLabel.setText(f'Vitórias: {self._activeAccount['win']}')
        self.backToMenuButton.setDisabled(False)
        self.startGame()
        
    def setGameVisible(self,value):
        self.answerButton.setDisabled(False)
        self.answerInput.setDisabled(False)
        self.answerButton.setDisabled(False)
        self.answerInput.setVisible(value)
        self.shotsLabel.setVisible(value)
        self.answerButton.setVisible(value)
        self.rangeLabel.setVisible(value)
        self.gameInfoLabel.setVisible(value)

    def saveAndBack(self):
        self.saveUserStats()
        self.setCurrentWidget(self.loginPage)
    
    def startGame(self):
        self.initLabel.setText('Escolha uma dificuldade')

        if self.currentWidget().objectName() != 'gamePage':
            self.setCurrentWidget(self.gamePage)
            self.setGameVisible(False)
            return
        
        dificultButtons = [self.easyButton,self.mediumButton,self.hardButton]

        self.answerButton.setDisabled(True)
        self.answerInput.setDisabled(True)

        for i in dificultButtons:
            i.setDisabled(False)
            i.setStyleSheet(f"""
                            QPushButton {{background-color: {PRIMARY_COLOR}}}
                            QPushButton:hover {{background: {DARKER_PRIMARY_COLOR};}}""")

    def saveUserStats(self):
        try:
            with open('contas.json', 'w', encoding='utf8') as file:
                json.dump(self._accounts,file,ensure_ascii=True,indent=2)
        except:
            print('Falha ao tentar realizar Backup')

    def recoverPassword(self):
        inputText = self.emailOrNickInput.text()
        userKey = ''

        if isValidEmail(inputText):
            userKey = 'email'
        else:
            userKey = 'login'

        for i in self._accounts:
            if i[userKey] == inputText:
                sendEmail(i)
                self.passRecInfo.setText("Senha enviada para o email cadastrado")
                return
        
        self.passRecInfo.setText(f"Não foi encontrado usuário com esse {userKey} cadastrado")
        
    def mainPageUpdate(self):
        self.winsLabel.setText(f'Vitórias: {self._activeAccount['win']}')
        self.lossLabel.setText(f'Derrotas: {self._activeAccount['loss']}')
        self.setCurrentWidget(self.mainPage)  

    def login(self):
        user = self.inputUser.text()
        password = self.inputPassword.text()
        print('procurando usuário', user,password)
        for i in self._accounts:
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
        
        for i in self._accounts:
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
        self._accounts.append(self._activeAccount)
        self.setCurrentWidget(self.mainPage)
        self.usernameLabel.setText(user)
        self.mainPageUpdate()

        
