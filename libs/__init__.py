import os
import sys
from libs.windows.Calculator import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

def restart(title, text):
   QMessageBox.information(calculator, title, text)
   sys.exit(0)
