from qt_material import apply_stylesheet

# Define as variáveis de cores que serão usadas no programa
PRIMARY_COLOR = '#1e81b0'
DARKER_PRIMARY_COLOR = '#16658a'
DARKEST_PRIMARY_COLOR = '#115270'
LM_BACKGROUND = '#FFF'
DM_BACKGROUND = '#1f1f1f'

# Define o Qss para o modo claro
lightQss = f"""
    QWidget{{
        background: {LM_BACKGROUND};
    }}


    QPushButton{{
        width: 120px;
        height: 40px;
        font-size: x-large;
        font-weight: 450;
        color: #fff;
        border: 2px solid {DARKEST_PRIMARY_COLOR};
        border-radius: 10px;
        background-color: {PRIMARY_COLOR};
    }}
    QPushButton:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]{{
        font-size: 13px;
        font-weight: 450;
        color: {PRIMARY_COLOR};
        background: {LM_BACKGROUND};
        border: 0px;
    }}
    QPushButton[cssClass="specialButton"]:hover{{
        color:{DARKEST_PRIMARY_COLOR};
    }}
    QPushButton:disabled {{
        background-color: {PRIMARY_COLOR};
    }}
    QLineEdit{{
        padding-left: 10px;
        border-radius: 10px;;
        width: 300px;
        height: 40px;
        font-size: larger;
        color: {DARKEST_PRIMARY_COLOR};
        border: 2px solid {PRIMARY_COLOR};

    }}
    QLabel{{
        color: {DARKEST_PRIMARY_COLOR};
        font-size: 20px;
    }}
    QLabel[cssClass="title"]{{
        font-weight: 400;
        font-size: 50px;
    }}
    QLabel[cssClass="warning"]{{
        color:red;
        font-size: 15px;
    }}
    QPushButton[cssClass="darkMode"]{{
        background: {LM_BACKGROUND};
        border: 5px;
        border-radius: 15px;
    }}

"""
# Define o Qss para o modo escuro
darkQss = f"""
    QWidget{{
        background: {DM_BACKGROUND};
    }}

    QPushButton{{
        width: 120px;
        height: 40px;
        font-size: x-large;
        font-weight: 450;
        color: #fff;
        border: 2px solid {DARKEST_PRIMARY_COLOR};
        border-radius: 10px;
        background-color: {PRIMARY_COLOR};
    }}
    QPushButton:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]{{
        font-size: 13px;
        font-weight: 450;
        color: {PRIMARY_COLOR};
        background: {DM_BACKGROUND};
        border: 0px;
    }}
    QPushButton[cssClass="specialButton"]:hover{{
        color:{DARKEST_PRIMARY_COLOR};
    }}
    QPushButton:disabled {{
        background-color: {PRIMARY_COLOR};
    }}
    QLineEdit{{
        padding-left: 10px;
        border-radius: 10px;;
        width: 300px;
        height: 40px;
        font-size: larger;
        color: {DARKEST_PRIMARY_COLOR};
        border: 2px solid {PRIMARY_COLOR};

    }}
    QLabel{{
        color: {DARKEST_PRIMARY_COLOR};
        font-size: 20px;
    }}
    QLabel[cssClass="title"]{{
        font-weight: 400;
        font-size: 50px;
    }}
    QLabel[cssClass="warning"]{{
        color:red;
        font-size: 15px;
    }}
    QPushButton[cssClass="darkMode"]{{
        background: {DM_BACKGROUND};
        border: 5px;
        border-radius: 15px;
    }}

"""

# Função que define o modo claro como ativo na aplicação
def setupLightTheme(app):

    app.setStyleSheet(app.styleSheet() + lightQss)

# Função que define o modo claro como escuro na aplicação
def setupDarkTheme(app):

    app.setStyleSheet(app.styleSheet() + darkQss)