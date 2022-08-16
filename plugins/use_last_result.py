"""
提供了使用上次计算结果作为下一个算式开头的功能
"""
from libs import *
from .copy_and_paste import _copy_action, _paste_action

__name__ = "使用上次计算结果"
__author__ = "此程序开发者"
__version__ = "1.0.0"

use_last_result_action = QAction("使用上次计算结果作为下一个算式开头", calculator.ui.functions_menu)
def _use_last_result_action():
    _copy_action()
    _paste_action()
use_last_result_action.triggered.connect(_use_last_result_action)

calculator.ui.functions_menu.addAction(use_last_result_action)
