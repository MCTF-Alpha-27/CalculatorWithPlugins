from libs.windows.Calculator import *

def exit_app(title, text):
   QMessageBox.information(calculator, title, text)
   calculator.setVisible(False)
   app.quit()
