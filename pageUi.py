# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesUi.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(500, 500)
        StackedWidget.setMinimumSize(QSize(500, 500))
        StackedWidget.setMaximumSize(QSize(500, 500))
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.loginPage.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.loginPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelInfo = QLabel(self.loginPage)
        self.labelInfo.setObjectName(u"labelInfo")
        self.labelInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labelInfo, 11, 0, 1, 1)

        self.inputPassword = QLineEdit(self.loginPage)
        self.inputPassword.setObjectName(u"inputPassword")
        self.inputPassword.setStyleSheet(u"")
        self.inputPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.inputPassword, 5, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.buttonLogin = QPushButton(self.loginPage)
        self.buttonLogin.setObjectName(u"buttonLogin")
        self.buttonLogin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonLogin.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.buttonLogin, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.buttonRegister = QPushButton(self.loginPage)
        self.buttonRegister.setObjectName(u"buttonRegister")
        self.buttonRegister.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonRegister.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.buttonRegister, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 8, 0, 1, 1)

        self.inputUser = QLineEdit(self.loginPage)
        self.inputUser.setObjectName(u"inputUser")
        self.inputUser.setStyleSheet(u"")

        self.gridLayout.addWidget(self.inputUser, 3, 0, 1, 1)

        self.labelPassword = QLabel(self.loginPage)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setStyleSheet(u"")

        self.gridLayout.addWidget(self.labelPassword, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 12, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.labelUser = QLabel(self.loginPage)
        self.labelUser.setObjectName(u"labelUser")
        self.labelUser.setStyleSheet(u"")
        self.labelUser.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelUser, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.forgetPassLabel = QPushButton(self.loginPage)
        self.forgetPassLabel.setObjectName(u"forgetPassLabel")
        self.forgetPassLabel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.forgetPassLabel)

        self.horizontalSpacer_6 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)

        self.labelTitle = QLabel(self.loginPage)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"")

        self.gridLayout.addWidget(self.labelTitle, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        StackedWidget.addWidget(self.loginPage)
        self.registerPage = QWidget()
        self.registerPage.setObjectName(u"registerPage")
        self.horizontalLayout_5 = QHBoxLayout(self.registerPage)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cadUserInfo = QLabel(self.registerPage)
        self.cadUserInfo.setObjectName(u"cadUserInfo")
        self.cadUserInfo.setMaximumSize(QSize(16777215, 20))
        self.cadUserInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_3.addWidget(self.cadUserInfo, 3, 0, 1, 1)

        self.cadConfPassLabel = QLabel(self.registerPage)
        self.cadConfPassLabel.setObjectName(u"cadConfPassLabel")

        self.gridLayout_3.addWidget(self.cadConfPassLabel, 10, 0, 1, 1)

        self.cadEmailLabel = QLabel(self.registerPage)
        self.cadEmailLabel.setObjectName(u"cadEmailLabel")

        self.gridLayout_3.addWidget(self.cadEmailLabel, 4, 0, 1, 1)

        self.cadPasswordLabel = QLabel(self.registerPage)
        self.cadPasswordLabel.setObjectName(u"cadPasswordLabel")

        self.gridLayout_3.addWidget(self.cadPasswordLabel, 7, 0, 1, 1)

        self.cadConfPassInput = QLineEdit(self.registerPage)
        self.cadConfPassInput.setObjectName(u"cadConfPassInput")
        self.cadConfPassInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_3.addWidget(self.cadConfPassInput, 11, 0, 1, 1)

        self.cadEmailInput = QLineEdit(self.registerPage)
        self.cadEmailInput.setObjectName(u"cadEmailInput")

        self.gridLayout_3.addWidget(self.cadEmailInput, 5, 0, 1, 1)

        self.cadasterTitle = QLabel(self.registerPage)
        self.cadasterTitle.setObjectName(u"cadasterTitle")

        self.gridLayout_3.addWidget(self.cadasterTitle, 0, 0, 1, 1)

        self.cadEmailInfo = QLabel(self.registerPage)
        self.cadEmailInfo.setObjectName(u"cadEmailInfo")
        self.cadEmailInfo.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_3.addWidget(self.cadEmailInfo, 6, 0, 1, 1)

        self.cadPageInfo = QLabel(self.registerPage)
        self.cadPageInfo.setObjectName(u"cadPageInfo")
        self.cadPageInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.cadPageInfo, 14, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.registerButton = QPushButton(self.registerPage)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.registerButton, 0, 1, 1, 1)

        self.backToLoginButton = QPushButton(self.registerPage)
        self.backToLoginButton.setObjectName(u"backToLoginButton")
        self.backToLoginButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.backToLoginButton, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 13, 0, 1, 1)

        self.cadUserLabel = QLabel(self.registerPage)
        self.cadUserLabel.setObjectName(u"cadUserLabel")

        self.gridLayout_3.addWidget(self.cadUserLabel, 1, 0, 1, 1)

        self.cadPasswordInput = QLineEdit(self.registerPage)
        self.cadPasswordInput.setObjectName(u"cadPasswordInput")
        self.cadPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_3.addWidget(self.cadPasswordInput, 8, 0, 1, 1)

        self.cadConfPassInfo = QLabel(self.registerPage)
        self.cadConfPassInfo.setObjectName(u"cadConfPassInfo")
        self.cadConfPassInfo.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_3.addWidget(self.cadConfPassInfo, 12, 0, 1, 1)

        self.cadUserInput = QLineEdit(self.registerPage)
        self.cadUserInput.setObjectName(u"cadUserInput")

        self.gridLayout_3.addWidget(self.cadUserInput, 2, 0, 1, 1)

        self.cadPassInfo = QLabel(self.registerPage)
        self.cadPassInfo.setObjectName(u"cadPassInfo")
        self.cadPassInfo.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_3.addWidget(self.cadPassInfo, 9, 0, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        StackedWidget.addWidget(self.registerPage)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.horizontalLayout_6 = QHBoxLayout(self.mainPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.usernameLabel = QLabel(self.mainPage)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setMaximumSize(QSize(16777215, 50))
        self.usernameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.usernameLabel, 2, 1, 1, 1)

        self.menuTitle = QLabel(self.mainPage)
        self.menuTitle.setObjectName(u"menuTitle")
        self.menuTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.menuTitle, 1, 1, 1, 1)

        self.winsLabel = QLabel(self.mainPage)
        self.winsLabel.setObjectName(u"winsLabel")
        self.winsLabel.setMaximumSize(QSize(16777215, 30))
        self.winsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.winsLabel, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 7, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_9, 3, 2, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.playButton = QPushButton(self.mainPage)
        self.playButton.setObjectName(u"playButton")

        self.gridLayout_6.addWidget(self.playButton, 0, 1, 1, 1)

        self.logoutButton = QPushButton(self.mainPage)
        self.logoutButton.setObjectName(u"logoutButton")

        self.gridLayout_6.addWidget(self.logoutButton, 1, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_10, 1, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_11, 1, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_6, 6, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 3, 0, 1, 1)

        self.lossLabel = QLabel(self.mainPage)
        self.lossLabel.setObjectName(u"lossLabel")
        self.lossLabel.setMaximumSize(QSize(16777215, 30))
        self.lossLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lossLabel, 4, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 5, 1, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_5)

        StackedWidget.addWidget(self.mainPage)
        self.gamePage = QWidget()
        self.gamePage.setObjectName(u"gamePage")
        self.horizontalLayout_2 = QHBoxLayout(self.gamePage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gameTitle = QLabel(self.gamePage)
        self.gameTitle.setObjectName(u"gameTitle")
        self.gameTitle.setMaximumSize(QSize(16777215, 40))
        self.gameTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.gameTitle)

        self.initLabel = QLabel(self.gamePage)
        self.initLabel.setObjectName(u"initLabel")
        self.initLabel.setMaximumSize(QSize(16777215, 20))
        self.initLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.initLabel)

        self.gameButtons = QHBoxLayout()
        self.gameButtons.setObjectName(u"gameButtons")
        self.easyButton = QPushButton(self.gamePage)
        self.easyButton.setObjectName(u"easyButton")
        self.easyButton.setEnabled(True)

        self.gameButtons.addWidget(self.easyButton)

        self.mediumButton = QPushButton(self.gamePage)
        self.mediumButton.setObjectName(u"mediumButton")
        self.mediumButton.setEnabled(True)

        self.gameButtons.addWidget(self.mediumButton)

        self.hardButton = QPushButton(self.gamePage)
        self.hardButton.setObjectName(u"hardButton")
        self.hardButton.setEnabled(True)

        self.gameButtons.addWidget(self.hardButton)


        self.verticalLayout.addLayout(self.gameButtons)

        self.shotInput = QLineEdit(self.gamePage)
        self.shotInput.setObjectName(u"shotInput")
        self.shotInput.setEnabled(False)

        self.verticalLayout.addWidget(self.shotInput)

        self.answerButton = QPushButton(self.gamePage)
        self.answerButton.setObjectName(u"answerButton")
        self.answerButton.setEnabled(False)

        self.verticalLayout.addWidget(self.answerButton)

        self.shotsLabel = QLabel(self.gamePage)
        self.shotsLabel.setObjectName(u"shotsLabel")
        self.shotsLabel.setMaximumSize(QSize(16777215, 20))
        self.shotsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.shotsLabel)

        self.gameInfoLabel = QLabel(self.gamePage)
        self.gameInfoLabel.setObjectName(u"gameInfoLabel")
        self.gameInfoLabel.setMaximumSize(QSize(16777215, 20))
        self.gameInfoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.gameInfoLabel)

        self.rangeLabel = QLabel(self.gamePage)
        self.rangeLabel.setObjectName(u"rangeLabel")
        self.rangeLabel.setMaximumSize(QSize(16777215, 20))
        self.rangeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.rangeLabel)

        self.backToMenuButton = QPushButton(self.gamePage)
        self.backToMenuButton.setObjectName(u"backToMenuButton")

        self.verticalLayout.addWidget(self.backToMenuButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        StackedWidget.addWidget(self.gamePage)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.labelInfo.setText("")
        self.buttonLogin.setText(QCoreApplication.translate("StackedWidget", u"Entrar", None))
        self.buttonRegister.setText(QCoreApplication.translate("StackedWidget", u"Cadastrar", None))
        self.labelPassword.setText(QCoreApplication.translate("StackedWidget", u"Senha", None))
        self.labelUser.setText(QCoreApplication.translate("StackedWidget", u"Usu\u00e1rio", None))
        self.forgetPassLabel.setText(QCoreApplication.translate("StackedWidget", u"Esqueceu sua senha?", None))
        self.labelTitle.setText(QCoreApplication.translate("StackedWidget", u"Login", None))
        self.cadUserInfo.setText("")
        self.cadConfPassLabel.setText(QCoreApplication.translate("StackedWidget", u"Confirme a senha", None))
        self.cadEmailLabel.setText(QCoreApplication.translate("StackedWidget", u"E-mail", None))
        self.cadPasswordLabel.setText(QCoreApplication.translate("StackedWidget", u"Senha", None))
        self.cadasterTitle.setText(QCoreApplication.translate("StackedWidget", u"Cadastrar", None))
        self.cadEmailInfo.setText("")
        self.cadPageInfo.setText("")
        self.registerButton.setText(QCoreApplication.translate("StackedWidget", u"Cadastrar", None))
        self.backToLoginButton.setText(QCoreApplication.translate("StackedWidget", u"Voltar", None))
        self.cadUserLabel.setText(QCoreApplication.translate("StackedWidget", u"Usu\u00e1rio", None))
        self.cadConfPassInfo.setText("")
        self.cadPassInfo.setText("")
        self.usernameLabel.setText("")
        self.menuTitle.setText(QCoreApplication.translate("StackedWidget", u"ADIVINHE O NUMERO", None))
        self.winsLabel.setText("")
        self.playButton.setText(QCoreApplication.translate("StackedWidget", u"Jogar", None))
        self.logoutButton.setText(QCoreApplication.translate("StackedWidget", u"Sair", None))
        self.lossLabel.setText("")
        self.gameTitle.setText(QCoreApplication.translate("StackedWidget", u"Adivinhe o Numero", None))
        self.initLabel.setText(QCoreApplication.translate("StackedWidget", u"TextLabel", None))
        self.easyButton.setText(QCoreApplication.translate("StackedWidget", u"F\u00e1cil", None))
        self.mediumButton.setText(QCoreApplication.translate("StackedWidget", u"M\u00e9dio", None))
        self.hardButton.setText(QCoreApplication.translate("StackedWidget", u"Dif\u00edcil", None))
        self.shotInput.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Digite um n\u00famero", None))
        self.answerButton.setText(QCoreApplication.translate("StackedWidget", u"Enviar palpite", None))
        self.shotsLabel.setText(QCoreApplication.translate("StackedWidget", u"Tentativas Restantes: XX", None))
        self.gameInfoLabel.setText(QCoreApplication.translate("StackedWidget", u"Errouuu", None))
        self.rangeLabel.setText(QCoreApplication.translate("StackedWidget", u"Intervalo: 1 a 100", None))
        self.backToMenuButton.setText(QCoreApplication.translate("StackedWidget", u"Voltar ao Menu", None))
    # retranslateUi

