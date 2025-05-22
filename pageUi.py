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
        self.horizontalLayout_12 = QHBoxLayout(self.loginPage)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.loginRegisterButton = QPushButton(self.loginPage)
        self.loginRegisterButton.setObjectName(u"loginRegisterButton")

        self.gridLayout_2.addWidget(self.loginRegisterButton, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.loginButton = QPushButton(self.loginPage)
        self.loginButton.setObjectName(u"loginButton")

        self.gridLayout_2.addWidget(self.loginButton, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 7, 1, 1, 1)

        self.loginLabelInfo = QLabel(self.loginPage)
        self.loginLabelInfo.setObjectName(u"loginLabelInfo")
        self.loginLabelInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.loginLabelInfo, 8, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 5, 2, 1, 1)

        self.loginUserInput = QLineEdit(self.loginPage)
        self.loginUserInput.setObjectName(u"loginUserInput")

        self.gridLayout.addWidget(self.loginUserInput, 3, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.forgetPassButton = QPushButton(self.loginPage)
        self.forgetPassButton.setObjectName(u"forgetPassButton")

        self.horizontalLayout_4.addWidget(self.forgetPassButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 4, 0, 1, 1)

        self.loginTitle = QLabel(self.loginPage)
        self.loginTitle.setObjectName(u"loginTitle")

        self.gridLayout.addWidget(self.loginTitle, 1, 1, 1, 1)

        self.loginPasswordInput = QLineEdit(self.loginPage)
        self.loginPasswordInput.setObjectName(u"loginPasswordInput")
        self.loginPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.loginPasswordInput, 5, 1, 1, 1)

        self.loginUserLabel = QLabel(self.loginPage)
        self.loginUserLabel.setObjectName(u"loginUserLabel")

        self.gridLayout.addWidget(self.loginUserLabel, 2, 1, 1, 1)

        self.loginPasswordLabel = QLabel(self.loginPage)
        self.loginPasswordLabel.setObjectName(u"loginPasswordLabel")

        self.gridLayout.addWidget(self.loginPasswordLabel, 4, 1, 1, 1)

        self.loginDarkMode = QPushButton(self.loginPage)
        self.loginDarkMode.setObjectName(u"loginDarkMode")
        self.loginDarkMode.setMaximumSize(QSize(30, 30))
        self.loginDarkMode.setCheckable(True)

        self.gridLayout.addWidget(self.loginDarkMode, 8, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.horizontalLayout_12.addLayout(self.verticalLayout_4)

        StackedWidget.addWidget(self.loginPage)
        self.registerPage = QWidget()
        self.registerPage.setObjectName(u"registerPage")
        self.horizontalLayout_5 = QHBoxLayout(self.registerPage)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cadEmailLabel = QLabel(self.registerPage)
        self.cadEmailLabel.setObjectName(u"cadEmailLabel")

        self.gridLayout_3.addWidget(self.cadEmailLabel, 4, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 5, 2, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.backToLoginButton = QPushButton(self.registerPage)
        self.backToLoginButton.setObjectName(u"backToLoginButton")

        self.horizontalLayout_9.addWidget(self.backToLoginButton)

        self.registerButton = QPushButton(self.registerPage)
        self.registerButton.setObjectName(u"registerButton")

        self.horizontalLayout_9.addWidget(self.registerButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_9, 13, 1, 1, 1)

        self.cadasterTitle = QLabel(self.registerPage)
        self.cadasterTitle.setObjectName(u"cadasterTitle")
        self.cadasterTitle.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.cadasterTitle, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 5, 0, 1, 1)

        self.cadPassInfo = QLabel(self.registerPage)
        self.cadPassInfo.setObjectName(u"cadPassInfo")

        self.gridLayout_3.addWidget(self.cadPassInfo, 9, 1, 1, 1)

        self.cadConfPassInfo = QLabel(self.registerPage)
        self.cadConfPassInfo.setObjectName(u"cadConfPassInfo")

        self.gridLayout_3.addWidget(self.cadConfPassInfo, 12, 1, 1, 1)

        self.cadConfPassLabel = QLabel(self.registerPage)
        self.cadConfPassLabel.setObjectName(u"cadConfPassLabel")

        self.gridLayout_3.addWidget(self.cadConfPassLabel, 10, 1, 1, 1)

        self.cadEmailInput = QLineEdit(self.registerPage)
        self.cadEmailInput.setObjectName(u"cadEmailInput")

        self.gridLayout_3.addWidget(self.cadEmailInput, 5, 1, 1, 1)

        self.cadUserLabel = QLabel(self.registerPage)
        self.cadUserLabel.setObjectName(u"cadUserLabel")

        self.gridLayout_3.addWidget(self.cadUserLabel, 1, 1, 1, 1)

        self.cadEmailInfo = QLabel(self.registerPage)
        self.cadEmailInfo.setObjectName(u"cadEmailInfo")

        self.gridLayout_3.addWidget(self.cadEmailInfo, 6, 1, 1, 1)

        self.cadPassLabel = QLabel(self.registerPage)
        self.cadPassLabel.setObjectName(u"cadPassLabel")

        self.gridLayout_3.addWidget(self.cadPassLabel, 7, 1, 1, 1)

        self.cadUserInfo = QLabel(self.registerPage)
        self.cadUserInfo.setObjectName(u"cadUserInfo")

        self.gridLayout_3.addWidget(self.cadUserInfo, 3, 1, 1, 1)

        self.cadPassInput = QLineEdit(self.registerPage)
        self.cadPassInput.setObjectName(u"cadPassInput")
        self.cadPassInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_3.addWidget(self.cadPassInput, 8, 1, 1, 1)

        self.cadUserInput = QLineEdit(self.registerPage)
        self.cadUserInput.setObjectName(u"cadUserInput")

        self.gridLayout_3.addWidget(self.cadUserInput, 2, 1, 1, 1)

        self.cadConfPassInput = QLineEdit(self.registerPage)
        self.cadConfPassInput.setObjectName(u"cadConfPassInput")
        self.cadConfPassInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_3.addWidget(self.cadConfPassInput, 11, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_3)

        self.cadDarkMode = QPushButton(self.registerPage)
        self.cadDarkMode.setObjectName(u"cadDarkMode")
        self.cadDarkMode.setMaximumSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.cadDarkMode)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

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

        self.gridLayout_5.addWidget(self.usernameLabel, 3, 1, 1, 1)

        self.lossLabel = QLabel(self.mainPage)
        self.lossLabel.setObjectName(u"lossLabel")
        self.lossLabel.setMaximumSize(QSize(16777215, 30))
        self.lossLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.lossLabel, 5, 1, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")

        self.gridLayout_5.addLayout(self.horizontalLayout_15, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 4, 0, 1, 1)

        self.winsLabel = QLabel(self.mainPage)
        self.winsLabel.setObjectName(u"winsLabel")
        self.winsLabel.setMaximumSize(QSize(16777215, 30))
        self.winsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.winsLabel, 4, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 1, 1, 1, 1)

        self.menuTitle = QLabel(self.mainPage)
        self.menuTitle.setObjectName(u"menuTitle")
        self.menuTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.menuTitle, 2, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_9, 4, 2, 1, 1)

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


        self.gridLayout_5.addLayout(self.gridLayout_6, 7, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 6, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 8, 1, 1, 1)

        self.menuDarkMode = QPushButton(self.mainPage)
        self.menuDarkMode.setObjectName(u"menuDarkMode")
        self.menuDarkMode.setMaximumSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.menuDarkMode, 9, 0, 1, 1)


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

        self.answerInput = QLineEdit(self.gamePage)
        self.answerInput.setObjectName(u"answerInput")
        self.answerInput.setEnabled(True)

        self.verticalLayout.addWidget(self.answerInput)

        self.answerButton = QPushButton(self.gamePage)
        self.answerButton.setObjectName(u"answerButton")
        self.answerButton.setEnabled(True)

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

        self.gameDarkMode = QPushButton(self.gamePage)
        self.gameDarkMode.setObjectName(u"gameDarkMode")
        self.gameDarkMode.setMaximumSize(QSize(30, 30))
        self.gameDarkMode.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout.addWidget(self.gameDarkMode)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        StackedWidget.addWidget(self.gamePage)
        self.passRecPage = QWidget()
        self.passRecPage.setObjectName(u"passRecPage")
        self.horizontalLayout_3 = QHBoxLayout(self.passRecPage)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.passRecTitle = QLabel(self.passRecPage)
        self.passRecTitle.setObjectName(u"passRecTitle")
        self.passRecTitle.setMaximumSize(QSize(16777215, 100))
        self.passRecTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.passRecTitle)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.emailOrNickLabel = QLabel(self.passRecPage)
        self.emailOrNickLabel.setObjectName(u"emailOrNickLabel")
        self.emailOrNickLabel.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.emailOrNickLabel)

        self.emailOrNickInput = QLineEdit(self.passRecPage)
        self.emailOrNickInput.setObjectName(u"emailOrNickInput")

        self.verticalLayout_3.addWidget(self.emailOrNickInput)

        self.sendEmailButton = QPushButton(self.passRecPage)
        self.sendEmailButton.setObjectName(u"sendEmailButton")

        self.verticalLayout_3.addWidget(self.sendEmailButton)

        self.backToLoginButton2 = QPushButton(self.passRecPage)
        self.backToLoginButton2.setObjectName(u"backToLoginButton2")

        self.verticalLayout_3.addWidget(self.backToLoginButton2)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.passRecInfo = QLabel(self.passRecPage)
        self.passRecInfo.setObjectName(u"passRecInfo")
        self.passRecInfo.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(5)
        self.passRecInfo.setFont(font)
        self.passRecInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.passRecInfo)

        self.recPassDarkMode = QPushButton(self.passRecPage)
        self.recPassDarkMode.setObjectName(u"recPassDarkMode")
        self.recPassDarkMode.setMaximumSize(QSize(30, 30))
        self.recPassDarkMode.setCheckable(True)

        self.verticalLayout_2.addWidget(self.recPassDarkMode)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        StackedWidget.addWidget(self.passRecPage)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.loginRegisterButton.setText(QCoreApplication.translate("StackedWidget", u"Cadastrar", None))
        self.loginButton.setText(QCoreApplication.translate("StackedWidget", u"Entrar", None))
        self.loginLabelInfo.setText("")
        self.forgetPassButton.setText(QCoreApplication.translate("StackedWidget", u"Esqueceu sua senha?", None))
        self.loginTitle.setText(QCoreApplication.translate("StackedWidget", u"Login", None))
        self.loginUserLabel.setText(QCoreApplication.translate("StackedWidget", u"Usu\u00e1rio", None))
        self.loginPasswordLabel.setText(QCoreApplication.translate("StackedWidget", u"Senha", None))
        self.loginDarkMode.setText("")
        self.cadEmailLabel.setText(QCoreApplication.translate("StackedWidget", u"Email", None))
        self.backToLoginButton.setText(QCoreApplication.translate("StackedWidget", u"Voltar", None))
        self.registerButton.setText(QCoreApplication.translate("StackedWidget", u"Cadastrar", None))
        self.cadasterTitle.setText(QCoreApplication.translate("StackedWidget", u"Cadastrar", None))
        self.cadPassInfo.setText("")
        self.cadConfPassInfo.setText("")
        self.cadConfPassLabel.setText(QCoreApplication.translate("StackedWidget", u"Confirme a senha", None))
        self.cadUserLabel.setText(QCoreApplication.translate("StackedWidget", u"Nome de usu\u00e1rio", None))
        self.cadEmailInfo.setText("")
        self.cadPassLabel.setText(QCoreApplication.translate("StackedWidget", u"Senha", None))
        self.cadUserInfo.setText("")
        self.cadDarkMode.setText("")
        self.usernameLabel.setText("")
        self.lossLabel.setText("")
        self.winsLabel.setText("")
        self.menuTitle.setText(QCoreApplication.translate("StackedWidget", u"ADIVINHE O NUMERO", None))
        self.playButton.setText(QCoreApplication.translate("StackedWidget", u"Jogar", None))
        self.logoutButton.setText(QCoreApplication.translate("StackedWidget", u"Sair", None))
        self.menuDarkMode.setText("")
        self.gameTitle.setText(QCoreApplication.translate("StackedWidget", u"Adivinhe o Numero", None))
        self.initLabel.setText(QCoreApplication.translate("StackedWidget", u"TextLabel", None))
        self.easyButton.setText(QCoreApplication.translate("StackedWidget", u"F\u00e1cil", None))
        self.mediumButton.setText(QCoreApplication.translate("StackedWidget", u"M\u00e9dio", None))
        self.hardButton.setText(QCoreApplication.translate("StackedWidget", u"Dif\u00edcil", None))
        self.answerInput.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Digite um n\u00famero", None))
        self.answerButton.setText(QCoreApplication.translate("StackedWidget", u"Enviar palpite", None))
        self.shotsLabel.setText("")
        self.gameInfoLabel.setText("")
        self.rangeLabel.setText("")
        self.backToMenuButton.setText(QCoreApplication.translate("StackedWidget", u"Voltar ao Menu", None))
        self.gameDarkMode.setText("")
        self.passRecTitle.setText(QCoreApplication.translate("StackedWidget", u"Recuperar senha", None))
        self.emailOrNickLabel.setText(QCoreApplication.translate("StackedWidget", u"Email ou nome de usu\u00e1rio", None))
        self.sendEmailButton.setText(QCoreApplication.translate("StackedWidget", u"Enviar", None))
        self.backToLoginButton2.setText(QCoreApplication.translate("StackedWidget", u"Voltar", None))
        self.passRecInfo.setText(QCoreApplication.translate("StackedWidget", u".", None))
        self.recPassDarkMode.setText("")
    # retranslateUi

