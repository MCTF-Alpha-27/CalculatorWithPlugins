from libs.windows.Calculator import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

def exit_app(title, text):
   QMessageBox.information(calculator, title, text)
   calculator.setVisible(False)
   app.quit()
