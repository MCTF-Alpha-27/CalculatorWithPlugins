"""
提供了退格功能
"""
from libs import *

__name__ = "退格"
__author__ = "此程序开发者"
__version__ = "1.0.0"

def action():
    try:
        calculator.ui.textEdit.setText(calculator.ui.textEdit.toPlainText()[:(len(calculator.ui.textEdit.toPlainText()) - 1)])
    except:
        pass

backspace_action = QAction("退格", calculator.ui.functions_menu)
backspace_action.triggered.connect(action)
calculator.ui.functions_menu.addAction(backspace_action)
