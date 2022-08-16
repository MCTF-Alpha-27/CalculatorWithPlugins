import sys
from libs import *

app = QApplication(sys.argv)

if __name__ == "__main__":
    import plugins
    calculator.show()
    sys.exit(app.exec())
