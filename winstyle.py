style = """QMainWindow {
    background-color: #FAFAFA;
    font-family: Segoe UI Semilight;
}

QLabel {
    font-family: Segoe UI Semilight;
    font-size: 14px;
}

QComboBox {
    height: 32px;
}

QAbstractButton {
    background-color: #BDBDBD;
    height: 32px;
    color: #000000;
    border-style: none;
    border-width: 0px;
    border-radius: 0px;
    font-size: 10pt;
    font-style: normal;
    padding-left: 10px;
    padding-right: 10px;
}

QAbstractButton:hover {
    border-style: outset;
    border-width: .1em;
    border-color: #000000;
}

QAbstractButton:pressed {
    border-style: none;
    background-color: #757575;
    border-radius: 2px;
}

QAbstractButton:disabled {
    color: #BDBDBD;
    background-color: #757575;
}

QPushButton {
    color: #FFFFFF;
    background-color: #0063B1;
}

QPushButton:pressed {
    background-color: #0078D7;
}

QComboBox
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    selection-background-color: #111;
    selection-color: #000000;
    color: black;
    background-color: #FFFFFF;
    border-style: solid;
    border: 2px solid #9E9E9E;
    border-radius: 0;
    font-size: 10pt;
    padding-left: 10px;
}


QComboBox:hover, QPushButton:hover
{
    border: 2px solid #000000;
}

QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 32px;
    height: 32px;
    color: white;
    border-left-width: 0px;
    border-left-color: darkgray;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
}

QComboBox QAbstractItemView {
    border: 2px solid darkgray;
    selection-background-color: lightgray;
}

QComboBox QAbstractItemView:item {
    padding-left: 10px;
    border: 2px solid darkgray;
    selection-background-color: lightgray;
}
"""
