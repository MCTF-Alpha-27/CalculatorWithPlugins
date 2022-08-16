from PyQt6.QtWidgets import *
from libs.gui.Calculator import Ui_Calculator

class Calculator(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.setWindowTitle("计算器")
        self.ui.pushButton_0.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_0))
        self.ui.pushButton_1.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_1))
        self.ui.pushButton_2.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_2))
        self.ui.pushButton_3.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_3))
        self.ui.pushButton_4.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_4))
        self.ui.pushButton_5.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_5))
        self.ui.pushButton_6.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_6))
        self.ui.pushButton_7.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_7))
        self.ui.pushButton_8.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_8))
        self.ui.pushButton_9.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_9))
        self.ui.pushButton_plus.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_plus))
        self.ui.pushButton_minus.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_minus))
        self.ui.pushButton_multiply.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_multiply))
        self.ui.pushButton_divide.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_divide))
        self.ui.pushButton_decimal_point.clicked.connect(lambda: self.set_pushButton_name_to_textEdit(self.ui.pushButton_decimal_point))
        self.ui.pushButton_equal.disconnect()
        self.ui.pushButton_equal.clicked.connect(self.on_pushButton_equal_clicked)

    def add_text_to_textEdit(self, text):
        self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + text)

    def set_pushButton_name_to_textEdit(self, pushButton: QPushButton):
        self.add_text_to_textEdit(pushButton.text())

    def on_pushButton_equal_clicked(self):
        if "=" in self.ui.textEdit.toPlainText() or self.ui.textEdit.toPlainText() == "":
            return
        try:
            result = eval(self.ui.textEdit.toPlainText())
            self.set_pushButton_name_to_textEdit(self.ui.pushButton_equal)
            self.add_text_to_textEdit(str(float(result)))
        except:
            self.ui.textEdit.setText("错误：算式无效")

app = QApplication([])
calculator = Calculator()
