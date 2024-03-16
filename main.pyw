import sys
from libs import *

app = QApplication(sys.argv)

if __name__ == "__main__":
    import plugins
    if len(sys.argv) > 1:
        if sys.argv[1] == "debug":
            calculator.debug = True
    calculator.show()
    sys.exit(app.exec())
