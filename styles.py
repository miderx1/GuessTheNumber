PRIMARY_COLOR = '#0f347a'
DARKER_PRIMARY_COLOR = '#0f347a'
DARKEST_PRIMARY_COLOR = '#0a2455'

qss = f"""
    QWidget{{
        background: {DARKEST_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"] {{
        width: 120px;
        height: 25px;
        font-size: x-large;
        font-weight: 450;
        color: rgb(15, 52, 122);
        border: 0;
        border-radius: 10px;
        background-color: rgb(255, 255, 255);
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="secondButton"]{{
        width: 120px;
        height: 25px;
        font-size: x-large;
        font-weight: 450;
        color: rgb(15, 52, 122);
        border: 0;
        border-radius: 10px;
    }}
    QPushButton[cssClass="secondButton"]:hover{{
        color:#FFF;
    }}
    QLineEdit[cssClass="logPageInput"]{{
        padding-left: 10px;
        border-radius: 10px;;
        width: 300px;
        height: 20px;
        font-size: larger;
        color: rgb(255, 255, 255);
        background: rgb(15, 52, 122);
        border: 0;
    }}
    QLabel[cssClass="logPageLabel"]{{
        color: #fff;
        font-size: 20px;
    }}
    QLabel[cssClass="title"]{{
        color: white;
        font-weight: 400;
        font-size: 50px;
    }}
    QLabel[cssClass="warning"]{{
        color:red;
    }}

"""

def setupTheme(app):
    app.setStyleSheet(app.styleSheet() + qss)