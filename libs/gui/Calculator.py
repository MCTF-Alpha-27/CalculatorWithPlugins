# Form implementation generated from reading ui file 'e:\bat\functions\Python\PyQtProject\Calculator\libs\gui\Calculator.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(331, 454)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 311, 71))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 100, 75, 71))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 100, 75, 71))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(170, 100, 75, 71))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 180, 75, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 180, 75, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 180, 75, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 260, 75, 71))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 260, 75, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 260, 75, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(250, 100, 75, 71))
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(250, 180, 75, 71))
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(250, 260, 75, 71))
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(250, 340, 75, 71))
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(90, 340, 75, 71))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(170, 340, 75, 71))
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_decimal_point = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decimal_point.setGeometry(QtCore.QRect(10, 340, 75, 71))
        self.pushButton_decimal_point.setObjectName("pushButton_decimal_point")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 22))
        self.menubar.setObjectName("menubar")
        self.functions_menu = QtWidgets.QMenu(self.menubar)
        self.functions_menu.setObjectName("functions_menu")
        self.plugins_menu = QtWidgets.QMenu(self.menubar)
        self.plugins_menu.setObjectName("plugins_menu")
        self.disabled_plugins_menu = QtWidgets.QMenu(self.menubar)
        self.disabled_plugins_menu.setObjectName("disabled_plugins_menu")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)
        self.menubar.addAction(self.functions_menu.menuAction())
        self.menubar.addAction(self.plugins_menu.menuAction())
        self.menubar.addAction(self.disabled_plugins_menu.menuAction())

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "MainWindow"))
        self.pushButton_7.setText(_translate("Calculator", "7"))
        self.pushButton_8.setText(_translate("Calculator", "8"))
        self.pushButton_9.setText(_translate("Calculator", "9"))
        self.pushButton_4.setText(_translate("Calculator", "4"))
        self.pushButton_5.setText(_translate("Calculator", "5"))
        self.pushButton_6.setText(_translate("Calculator", "6"))
        self.pushButton_1.setText(_translate("Calculator", "1"))
        self.pushButton_2.setText(_translate("Calculator", "2"))
        self.pushButton_3.setText(_translate("Calculator", "3"))
        self.pushButton_divide.setText(_translate("Calculator", "/"))
        self.pushButton_multiply.setText(_translate("Calculator", "*"))
        self.pushButton_minus.setText(_translate("Calculator", "-"))
        self.pushButton_plus.setText(_translate("Calculator", "+"))
        self.pushButton_0.setText(_translate("Calculator", "0"))
        self.pushButton_equal.setText(_translate("Calculator", "="))
        self.pushButton_decimal_point.setText(_translate("Calculator", "."))
        self.functions_menu.setTitle(_translate("Calculator", "功能"))
        self.plugins_menu.setTitle(_translate("Calculator", "插件"))
        self.disabled_plugins_menu.setTitle(_translate("Calculator", "禁用的插件"))
