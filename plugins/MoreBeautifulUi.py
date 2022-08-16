"""
修改了原来计算器的UI，使其变得更好看
"""
from libs import *

__name__ = "更好的UI"
__author__ = "此程序开发者"
__version__ = "1.0.0"

style = """
#Calculator {
    background-color: beige;
}

.QPushButton {
    background-color: #b49068;
}

.QPushButton:hover {
    background-color: aqua;
}

#textEdit {
    width: 290px;
    height: 30px;
    border: none;
    border-radius: 0%;
    font-size: 20px;
    color: black;
}
"""

calculator.setStyleSheet(style)
