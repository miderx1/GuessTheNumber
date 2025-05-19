from qt_material import apply_stylesheet

PRIMARY_COLOR = '#76A5D3'
DARKER_PRIMARY_COLOR = '#4B82BB'
DARKEST_PRIMARY_COLOR = '#284E7C'

lightQss = f"""
    QWidget{{
        background: #fff;
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
        background: #fff;
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

"""

def setupTheme(app):

    app.setStyleSheet(app.styleSheet() + lightQss)