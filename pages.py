from pageUi import Ui_StackedWidget
from styles import PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,DARKER_PRIMARY_COLOR, setupDarkTheme, setupLightTheme
from utils import isValidEmail
from emailSender import sendEmail
from PySide6.QtWidgets import QStackedWidget, QApplication
from PySide6.QtGui import QIcon
import json
import random
from pathlib import Path

# Cria variáveis com o caminho dos icones do botão de modo escuro e modo claro
DARK_MODE_ICON_PATH = Path(__file__).parent / 'src' / 'darkMode.png'
LIGHT_MODE_ICON_PATH = Path(__file__).parent / 'src' / 'lightMode.png'

# Criação da janela do programa
class Main_Window(Ui_StackedWidget,QStackedWidget):
    def __init__(self,accounts:list, parent=None, ):

        super().__init__(parent)
        self.setupUi(self)
        self._accounts = accounts # Recebe as contas cadastradas
        self._activeAccount = {} # Irá receber a conta que está logada no momento
        self._shots = 0 # Irá receber a quantidade de tentativas restantes do usuário
        self._randomNumber = 0  # Receberá o número sorteado, o qual o usuário terá que adivinhar
        self._gameRange = 0 # Receberá o intervalo em que se encontra o número sorteado
        self._darkmode = False  # Variável responsável por definir se o modo escuro está ativado

        # Define classes de Css para os componentes da paginas
        self.loginTitle.setProperty('cssClass','title') 
        self.loginRegisterButton.setProperty('cssClass','specialButton')
        self.forgetPassButton.setProperty('cssClass','specialButton')
        self.loginLabelInfo.setProperty('cssClass','warning')
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

        self.loginDarkMode.setProperty('cssClass','darkMode')
        self.recPassDarkMode.setProperty('cssClass','darkMode')
        self.cadDarkMode.setProperty('cssClass','darkMode')
        self.menuDarkMode.setProperty('cssClass','darkMode')
        self.gameDarkMode.setProperty('cssClass','darkMode')

        # Define o ícone do botão de modo escuro
        self.setDarkModeIcon(DARK_MODE_ICON_PATH)


        # Conecta os botões de troca de tela aos métodos de troca de tela
        self.loginRegisterButton.clicked.connect(lambda: self.setCurrentWidget(self.registerPage))
        self.forgetPassButton.clicked.connect(lambda: self.setCurrentWidget(self.passRecPage))
        self.backToLoginButton.clicked.connect(lambda: self.setCurrentWidget(self.loginPage))
        self.backToMenuButton.clicked.connect(lambda: self.setCurrentWidget(self.mainPage))
        self.backToLoginButton2.clicked.connect(self.backToLoginPage)

        # Conecta os demais botões do programa aos seus devidos métodos.
        self.logoutButton.clicked.connect(self.saveAndBack)
        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)
        self.playButton.clicked.connect(self.showDifficults)
        self.answerButton.clicked.connect(self.sendAnswer)
        self.sendEmailButton.clicked.connect(self.recoverPassword)

        self.easyButton.clicked.connect(self.play)
        self.mediumButton.clicked.connect(self.play)
        self.hardButton.clicked.connect(self.play)
        

        # Conecta todos os botões de modo escuro ao método de modo escuro
        self.loginDarkMode.clicked.connect(self.darkMode)
        self.recPassDarkMode.clicked.connect(self.darkMode)
        self.cadDarkMode.clicked.connect(self.darkMode)
        self.gameDarkMode.clicked.connect(self.darkMode)
        self.menuDarkMode.clicked.connect(self.darkMode)

    # Método que muda os ícones dos botões de modo escuro
    def setDarkModeIcon(self,iconPath):
        self.loginDarkMode.setIcon(QIcon(str(iconPath)))
        self.recPassDarkMode.setIcon(QIcon(str(iconPath)))
        self.cadDarkMode.setIcon(QIcon(str(iconPath)))
        self.menuDarkMode.setIcon(QIcon(str(iconPath)))
        self.gameDarkMode.setIcon(QIcon(str(iconPath)))

    # Método que ativa ou desativa o modo escuro
    def darkMode(self):

        # Cria uma variável que recebe a instância da própria aplicação

        app = QApplication.instance()
        
        # Verifica se o modo escuro já está ativado.
        if self._darkmode:
            setupLightTheme(app) # Ativa na aplicação o modo claro
            self._darkmode = False # Altera a variável que verifica se o modo escuro está ativado para False 
            self.setDarkModeIcon(DARK_MODE_ICON_PATH) # Muda o ícone do botão de modo escuro
            return
        
        # Caso o modo escuro não esteja ativado, vai ativar.
        setupDarkTheme(app)
        self._darkmode = True  # Altera a variável que verifica se o modo escuro está ativado para True
        
        self.setDarkModeIcon(LIGHT_MODE_ICON_PATH) # Muda o ícone do botão de modo escuro
        
    # Método que volta para a pagina de login,
    # e limpa as labels e inputs que tinham texto
    def backToLoginPage(self):
        self.passRecInfo.clear()
        self.emailOrNickInput.clear()
        self.setCurrentWidget(self.loginPage)

    # Método que muda a visibilidade dos componentes da pagina de jogo
    def setGameVisible(self,value):
        self.answerButton.setDisabled(False)
        self.answerInput.setDisabled(False)
        self.answerButton.setDisabled(False)
        self.answerInput.setVisible(value)
        self.shotsLabel.setVisible(value)
        self.answerButton.setVisible(value)
        self.rangeLabel.setVisible(value)
        self.gameInfoLabel.setVisible(value)

    # Método que inicia o jogo
    def play(self):

        # Desabilita o botão de voltar ao menu enquanto o jogo estiver rodando.
        self.backToMenuButton.setDisabled(True)
        self._shots = 10 # Define 10 tentativas para o usuário
        button = self.sender() # variável recebe o botão que ativou o método
        # Limpa a label que dizia para escolher a dificuldade
        self.gameInfoLabel.clear()  
        # Muda a cor da label informativa
        self.gameInfoLabel.setStyleSheet(f'color: {DARKEST_PRIMARY_COLOR}')         

        # Cria uma lista com os três botões de dificuldade
        dificultButtons = [self.easyButton,self.mediumButton,self.hardButton]

        # Cria um dicionário contendo as três dificuldades 
        # e seus respectivos intervalos numéricos
        dificults = {
            'Fácil' : 100,
            'Médio' : 150,
            'Difícil' : 200
        }

        # Verifica qual dos botões foram apertados e muda a cor dele,
        # e deixa todos os botões desativados, para impossibilitar
        # a mudança de dificuldade durante o jogo
        for i in dificultButtons:
            if button.text() == i.text():
                self._gameRange = dificults[button.text()]
                button.setStyleSheet(f'background-color: {DARKEST_PRIMARY_COLOR}')

            i.setDisabled(True)

        # Sorteia um número para o jogo informa que o número foi sorteado
        # e as tentativas restantes
        self._randomNumber = random.randint(1,self._gameRange)
        self.initLabel.setText('número sorteado')
        self.rangeLabel.setText(f'Intervalo: 1 até {self._gameRange}')
        self.shotsLabel.setText(f'Tentativas restantes: {self._shots}')

        # Deixa visível o jogo, após o usuário escolher a dificuldade
        self.setGameVisible(True)

    # Função que envia a resposta do usuário e verifica se está correta
    def sendAnswer(self):
        
        # Armazena o numero digitado numa variável 
        # e depois limpa o input
        answer = self.answerInput.text()
        self.answerInput.clear()

        # Verifica se o valor digitado é um número válido.
        # caso seja, irá criar a variável que diz se o numero é 
        # maior ou menor que o sorteado
        try:
            smallerOrBigger = 'maior' if int(answer) < self._randomNumber else 'menor'
        except ValueError:
            self.gameInfoLabel.setText('número inválido')
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
        
        # Verifica se o número está fora do intervalo informado
        elif int(answer) > self._gameRange or int(answer) < 0:
            self.gameInfoLabel.setText('número fora do intervalo')
            return
        
        # Verifica se o número é maior ou menor que o valor sorteado
        elif int(answer) > self._randomNumber or int(answer) < self._randomNumber:
            self._shots -= 1  # Diminui uma tentativa do usuário

            # Verifica se o usuário tem mais de 1 tentativa restante.
            # Caso tenha,  informará que o numero é maior ou menor que o sorteado
            if self._shots > 1 :
                self.gameInfoLabel.setText(f'Errou! o número sorteado é {smallerOrBigger} que {answer}')
                self.shotsLabel.setText(f'Tentativas restantes: {self._shots}')
                return

            # Caso o usuário n tenha mais tentativas, irá mudar a cor do texto
            # informativo para velho e irá avisar que ele perdeu, pois acabou
            # as tentativas. Logo após irá acrescentar uma derrota aos dados do
            # usuário e irá ativar os botôes de dificuldades e de voltar para o menu
            self.gameInfoLabel.setStyleSheet('color: red')
            self.gameInfoLabel.setText(f'Você perdeu! Tentativas esgotadas.')
            self._activeAccount['loss'] += 1
            self.lossLabel.setText(f'Derrotas: {self._activeAccount['loss']}')
            self.shotsLabel.setText(f'Tentativas restantes: {self._shots}')
            self.backToMenuButton.setDisabled(False)
            self.showDifficults()
            return
        
        # Caso o numero estiver correto, irá mudar a cor do texto informativo
        # para verde e informará que o usuário ganhou,
        # Logo após, irá acrescentar uma vitórias aos dados do usuário e
        # ativar os bototes de dificuldades e de voltar para o menu principal.
        self.gameInfoLabel.setStyleSheet('color: green')
        self.gameInfoLabel.setText(f'Você acertou! o número sorteado era {answer}')
        self._activeAccount['win'] += 1
        self.winsLabel.setText(f'Vitórias: {self._activeAccount['win']}')
        self.backToMenuButton.setDisabled(False)
        self.showDifficults()

    # Método que salva os dados do usuário em um arquivo JSON, junto com as
    # outras contas cadastradas
    def saveUserStats(self):
        try:
            with open('contas.json', 'w', encoding='utf8') as file:
                json.dump(self._accounts,file,ensure_ascii=True,indent=2)
        except:
            print('Falha ao tentar realizar Backup')

    # Método que salva o os dados do usuário e volta para a tela de login
    def saveAndBack(self):
        self.saveUserStats()
        self.setCurrentWidget(self.loginPage)
    
    # Método que mua para a tela do jogo e mostra os botões para
    # o usuário escolher a dificuldade

    def showDifficults(self):
        self.initLabel.setText('Escolha uma dificuldade')

        # Verifica se o usuário não está na tela do jogo.
        # Caso esteja, mudará para a tela do jogo
        if self.currentWidget().objectName() != 'gamePage':
            self.setCurrentWidget(self.gamePage)
            self.setGameVisible(False)
            return
        
        # Cria uma lista com os botões de dificuldades
        dificultButtons = [self.easyButton,self.mediumButton,self.hardButton]

        # Desabilita o botão e o input de resposta
        self.answerButton.setDisabled(True)
        self.answerInput.setDisabled(True)

        # Restaura o styleSheet dos botões para o padrão normal
        for i in dificultButtons:
            i.setDisabled(False)
            i.setStyleSheet(f"""
                            QPushButton {{background-color: {PRIMARY_COLOR}}}
                            QPushButton:hover {{background: {DARKER_PRIMARY_COLOR};}}""")

    # Método que recupera a senha perdida do usuário
    def recoverPassword(self):

        # Variável que armazena o texto digitado pelo usuário
        inputText = self.emailOrNickInput.text()
        userKey = '' # Cria uma variável pra armazenar qual chave do dicionario o usuário digitou

        # Verifica se o usuário digitou um email ou um nome de usuário
        if isValidEmail(inputText):
            userKey = 'email'
        else:
            userKey = 'login'

        # Verifica em todas as contas se existe um usuário com o email ou
        # nome de usuário digitado. Caso tenha, enviará um email  com a senha
        # para o endereço cadastrado na conta
        for i in self._accounts:
            if i[userKey] == inputText:
                sendEmail(i)
                self.passRecInfo.setText("Senha enviada para o email cadastrado")
                return
        
        # Caso não ache uma conta com o Email/Nome de usuário, informará
        # que não existe usuário com o dado informado
        self.passRecInfo.setText(f"Não foi encontrado usuário com esse {userKey} cadastrado")
    
    # Método que atualiza as informações da tela do menu, com as vitórias
    # e derrotas do usuário
    def mainPageUpdate(self):
        self.winsLabel.setText(f'Vitórias: {self._activeAccount['win']}')
        self.lossLabel.setText(f'Derrotas: {self._activeAccount['loss']}')
        self.setCurrentWidget(self.mainPage)  

    # Método que loga o usuário no jogo
    def login(self):
        # Variáveis que armazenam o login e senha digitados pelo usuário
        user = self.loginUserInput.text()
        password = self.loginPasswordInput.text()

        # Procura na lista de contas o usuário com o login informado.
        # Após encontrar, irá verificar se a senha informada confere
        # com a senha cadastrada na conta
        for i in self._accounts:
            if i['login'] == user:
                
                if i['senha'] == password:
                    
                    # Armazena o usuário encontrado como ativo
                    self._activeAccount = i  
                    self.usernameLabel.setText(user.upper())
                    self.mainPageUpdate()
                    self.loginLabelInfo.clear()
                    return
                
                # Caso a senha esteja incorreta, irá informar ao usuário
                self.loginLabelInfo.setText('Senha incorreta')
                return
        
        # Caso não ache um usuário com o login informado, avisará na tela.
        self.loginLabelInfo.setText('Usuário não encontrado')

    # Método que cadastra o usuário
    def register(self):

        # Limpa todos os textos informativos
        self.cadUserInfo.clear()
        self.cadPassInfo.clear()
        self.cadEmailInfo.clear()
        self.cadConfPassInfo.clear()

        # Armazena nas variáveis os dados informados pelo usuário 
        user = self.cadUserInput.text()
        password = self.cadPassInput.text()
        email = self.cadEmailInput.text()
        confPassword = self.cadConfPassInput.text()
        
        # Verifica se o usuário não digitou um nome de usuário
        if not user:
            self.cadUserInfo.setText('Preencha esse campo')
            return
        
        # Verifica na lista de contas se já existe um usuário com o
        # login ou email informado
        for i in self._accounts:
            if user == i['login']:
                self.cadUserInfo.setText('Usuário já cadastrado')
                return
            if email == i['email']:
                self.cadEmailInfo.setText('Email já cadastrado')
                return
        # Verifica se o usuário não digitou um email
        if not email:
            self.cadEmailInfo.setText('Preencha esse campo')
            return
        # Verifica se o email digitado é válido
        elif not isValidEmail(email):
            self.cadEmailInfo.setText('Email inválido')
            return
        # Verifica se o usuário não digitou uma senha
        if not password:
            self.cadPassInfo.setText('Preencha esse campo')
            return
        
        # Verifica se a senha e a confirmação da senha não conferem
        if password != confPassword:
            self.cadConfPassInfo.setText('Senhas não conferem')
            return

        # Após passar por todas as verificações, criará um usuário com os dados
        # informados.
        activeUser = dict(
            login = user,
            senha = password,
            email = email,
            win = 0,
            loss = 0,
        )

        # Colocará o usuário recém-criado como jogador ativo
        self._activeAccount = activeUser
        # Adicionará o usuário na lista de contas cadastradas
        self._accounts.append(self._activeAccount)
        # Mudará para a tela do menu do jogo, já logado.
        self.setCurrentWidget(self.mainPage)
        # Atualizará a tela do menu com os dados do usuário
        self.usernameLabel.setText(user)
        self.mainPageUpdate()

        
