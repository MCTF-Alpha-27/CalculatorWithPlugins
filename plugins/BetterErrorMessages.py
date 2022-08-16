"""
当你输入无效算式时计算器就会被玩坏
"""
from libs import *

__name__ = "更好的错误信息"
__author__ = "此程序开发者"
__version__ = "1.0.0"

def on_textEdit_textChanged():
    if "错误" in calculator.ui.textEdit.toPlainText():
        calculator.ui.textEdit.setText("被~被玩坏了啊❤~")

calculator.ui.textEdit.textChanged.connect(on_textEdit_textChanged)
