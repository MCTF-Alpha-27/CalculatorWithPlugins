"""
提供了清零功能
"""
from libs import *

__name__ = "清零"
__author__ = "此程序开发者"
__version__ = "1.0.0"

CE_action = QAction("清零", calculator.ui.functions_menu)
CE_action.triggered.connect(lambda: calculator.ui.textEdit.setText(""))
calculator.ui.functions_menu.addAction(CE_action)
