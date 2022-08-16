"""
提供了复制结果&黏贴算式的功能
"""
from libs import *
import pyperclip

__name__ = "复制&黏贴"
__author__ = "此程序开发者"
__version__ = "1.0.0"

copy_and_paste_menu = QMenu("复制&黏贴", calculator.ui.functions_menu)
calculator.ui.functions_menu.addMenu(copy_and_paste_menu)

copy_action = QAction("复制结果", copy_and_paste_menu)
def _copy_action():
    if "=" not in calculator.ui.textEdit.toPlainText():
        return
    text = ""
    for i in calculator.ui.textEdit.toPlainText().split("=")[1]:
        if i.isdigit() or i == ".":
            text += i
    pyperclip.copy(text)
copy_action.triggered.connect(_copy_action)
copy_and_paste_menu.addAction(copy_action)

paste_action = QAction("黏贴算式", copy_and_paste_menu)
def _paste_action():
    for i in pyperclip.paste():
        if not (i.isdigit() or i in ["+", "-", "*", "/", "."]):
            return
    calculator.ui.textEdit.setText(pyperclip.paste())
paste_action.triggered.connect(_paste_action)
copy_and_paste_menu.addAction(paste_action)
