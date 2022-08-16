"""
哼哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
当你的计算结果出现homo要素时，计算器会表示很臭
"""
from libs import *

__name__ = "homo数监听器"
__author__ = "此程序开发者"
__version__ = "1.0.0"

def on_textEdit_textChanged():
    text = calculator.ui.textEdit.toPlainText()
    if "=" in text and "臭" not in text:
        for i in ["114514", "1919810"]:
            if i in text.split("=")[1]:
                calculator.add_text_to_textEdit("\n这个结果怎么这么臭啊（恼")
                break

calculator.ui.textEdit.textChanged.connect(on_textEdit_textChanged)
