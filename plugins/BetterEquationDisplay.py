"""
修改了原来计算器的算式显示，使其变得更好看
"""
from libs import *

__name__ = "更好的算式显示"
__author__ = "此程序开发者"
__version__ = "1.0.0"

calculator.ui.pushButton_divide.setText("÷")
calculator.ui.pushButton_multiply.setText("×")

def on_pushButton_equal_clicked():
    if "=" in calculator.ui.textEdit.toPlainText() or calculator.ui.textEdit.toPlainText() == "":
        return
    try:
        result = eval(calculator.ui.textEdit.toPlainText().replace("÷", "/").replace("×", "*"))
        calculator.set_pushButton_name_to_textEdit(calculator.ui.pushButton_equal)
        calculator.add_text_to_textEdit(str(float(result)))
    except:
        calculator.ui.textEdit.setText("错误：算式无效")

calculator.ui.pushButton_equal.clicked.disconnect(calculator.on_pushButton_equal_clicked)
calculator.ui.pushButton_equal.clicked.connect(on_pushButton_equal_clicked)
