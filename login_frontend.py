# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LMSlogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from utils import get_user_names, create_new_user, update_password, validate_user
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("LMS LOGIN")
        Dialog.resize(1366, 768)
        Dialog.setMinimumSize(QtCore.QSize(1366, 768))
        Dialog.setMaximumSize(QtCore.QSize(1366, 768))
        self.bg_label = QtWidgets.QLabel(Dialog)
        self.bg_label.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.bg_label.setText("")
        self.bg_label.setPixmap(QtGui.QPixmap("Assets/Web 1920 – 1.png"))
        self.bg_label.setObjectName("bg_label")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(800, 210, 411, 331))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 157, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 236, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 196, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 78, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 105, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 157, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 206, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 157, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 236, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 196, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 78, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 105, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 157, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 206, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 78, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 157, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 236, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 196, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 78, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 105, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 78, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 78, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 157, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 157, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 157, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.usr_label = QtWidgets.QLabel(self.login)
        self.usr_label.setGeometry(QtCore.QRect(20, 20, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.usr_label.setFont(font)
        self.usr_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.usr_label.setObjectName("usr_label")
        self.pass_label = QtWidgets.QLabel(self.login)
        self.pass_label.setGeometry(QtCore.QRect(20, 130, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pass_label.setFont(font)
        self.pass_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pass_label.setObjectName("pass_label")
        self.pass_box = QtWidgets.QLineEdit(self.login)
        self.pass_box.setGeometry(QtCore.QRect(40, 180, 311, 31))
        self.pass_box.setObjectName("pass_box")
        self.usr_cbox = QtWidgets.QComboBox(self.login)
        self.usr_cbox.setGeometry(QtCore.QRect(40, 70, 311, 31))
        self.usr_cbox.setEditable(True)
        self.usr_cbox.setObjectName("usr_cbox")
        for usr in get_user_names():
            self.usr_cbox.addItem(usr)

        self.login_btn = QtWidgets.QPushButton(self.login)
        self.login_btn.setGeometry(QtCore.QRect(270, 230, 81, 23))
        self.login_btn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.login_btn.setFlat(False)
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.onclick_login)

        self.tabWidget.addTab(self.login, "")
        self.register = QtWidgets.QWidget()
        self.register.setObjectName("register")
        self.name_label = QtWidgets.QLabel(self.register)
        self.name_label.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.name_box = QtWidgets.QLineEdit(self.register)
        self.name_box.setGeometry(QtCore.QRect(20, 50, 281, 21))
        self.name_box.setObjectName("name_box")
        self.desi_label = QtWidgets.QLabel(self.register)
        self.desi_label.setGeometry(QtCore.QRect(20, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.desi_label.setFont(font)
        self.desi_label.setObjectName("desi_label")
        self.desi_cbox = QtWidgets.QComboBox(self.register)
        self.desi_cbox.setGeometry(QtCore.QRect(20, 110, 281, 22))
        self.desi_cbox.setObjectName("desi_cbox")
        self.desi_cbox.addItem("")
        self.desi_cbox.addItem("")
        self.desi_cbox.addItem("")
        self.desi_cbox.addItem("")
        self.rusr_label = QtWidgets.QLabel(self.register)
        self.rusr_label.setGeometry(QtCore.QRect(20, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rusr_label.setFont(font)
        self.rusr_label.setObjectName("rusr_label")
        self.rusr_box = QtWidgets.QLineEdit(self.register)
        self.rusr_box.setGeometry(QtCore.QRect(20, 170, 281, 21))
        self.rusr_box.setObjectName("rusr_box")
        self.rpass_label = QtWidgets.QLabel(self.register)
        self.rpass_label.setGeometry(QtCore.QRect(20, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.rpass_label.setFont(font)
        self.rpass_label.setObjectName("rpass_label")
        self.rpass_box = QtWidgets.QLineEdit(self.register)
        self.rpass_box.setGeometry(QtCore.QRect(20, 230, 131, 21))
        self.rpass_box.setObjectName("rpass_box")
        self.concpass_label = QtWidgets.QLabel(self.register)
        self.concpass_label.setGeometry(QtCore.QRect(170, 200, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.concpass_label.setFont(font)
        self.concpass_label.setObjectName("concpass_label")
        self.concpass_box = QtWidgets.QLineEdit(self.register)
        self.concpass_box.setGeometry(QtCore.QRect(170, 230, 131, 21))
        self.concpass_box.setObjectName("concpass_box")

        self.register_btn = QtWidgets.QPushButton(self.register)
        self.register_btn.setGeometry(QtCore.QRect(280, 270, 75, 23))
        self.register_btn.setObjectName("register_btn")
        self.register_btn.clicked.connect(self.onclick_register)

        self.tabWidget.addTab(self.register, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.fname_label = QtWidgets.QLabel(self.tab_3)
        self.fname_label.setGeometry(QtCore.QRect(20, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fname_label.setFont(font)
        self.fname_label.setObjectName("fname_label")
        self.fname_box = QtWidgets.QLineEdit(self.tab_3)
        self.fname_box.setGeometry(QtCore.QRect(20, 40, 281, 21))
        self.fname_box.setObjectName("fname_box")
        self.fusr_label = QtWidgets.QLabel(self.tab_3)
        self.fusr_label.setGeometry(QtCore.QRect(20, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fusr_label.setFont(font)
        self.fusr_label.setObjectName("fusr_label")
        self.fusrname_box = QtWidgets.QLineEdit(self.tab_3)
        self.fusrname_box.setGeometry(QtCore.QRect(20, 110, 281, 21))
        self.fusrname_box.setObjectName("fusrname_box")
        self.fpass_label = QtWidgets.QLabel(self.tab_3)
        self.fpass_label.setGeometry(QtCore.QRect(20, 150, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fpass_label.setFont(font)
        self.fpass_label.setObjectName("fpass_label")
        self.fpass_box = QtWidgets.QLineEdit(self.tab_3)
        self.fpass_box.setGeometry(QtCore.QRect(20, 180, 281, 21))
        self.fpass_box.setObjectName("fpass_box")
        self.fconcpass_label = QtWidgets.QLabel(self.tab_3)
        self.fconcpass_label.setGeometry(QtCore.QRect(20, 220, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fconcpass_label.setFont(font)
        self.fconcpass_label.setObjectName("fconcpass_label")
        self.fconcpass_box = QtWidgets.QLineEdit(self.tab_3)
        self.fconcpass_box.setGeometry(QtCore.QRect(20, 250, 281, 21))
        self.fconcpass_box.setObjectName("fconcpass_box")

        self.finish_btn = QtWidgets.QPushButton(self.tab_3)
        self.finish_btn.setGeometry(QtCore.QRect(290, 290, 75, 23))
        self.finish_btn.setObjectName("finish_btn")
        self.finish_btn.clicked.connect(self.onclick_forgot_finish)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.usr_label.setText(_translate("Dialog", "USERNAME"))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))
        self.login_btn.setText(_translate("Dialog", "LOGIN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login), _translate("Dialog", "LOGIN"))
        self.name_label.setText(_translate("Dialog", "NAME"))
        self.desi_label.setText(_translate("Dialog", "DESIGNATION"))
        self.desi_cbox.setItemText(0, _translate("Dialog", "Assistant Professor"))
        self.desi_cbox.setItemText(1, _translate("Dialog", "Head of Department"))
        self.desi_cbox.setItemText(2, _translate("Dialog", "Student"))
        self.desi_cbox.setItemText(3, _translate("Dialog", "Librarian"))
        self.rusr_label.setText(_translate("Dialog", "USERNAME"))
        self.rpass_label.setText(_translate("Dialog", "PASSWORD"))
        self.concpass_label.setText(_translate("Dialog", "CONFIRM PASSWORD"))
        self.register_btn.setText(_translate("Dialog", "REGISTER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.register), _translate("Dialog", "REGISTER"))
        self.fname_label.setText(_translate("Dialog", "NAME"))
        self.fusr_label.setText(_translate("Dialog", "USERNAME"))
        self.fpass_label.setText(_translate("Dialog", "NEW PASSWORD"))
        self.fconcpass_label.setText(_translate("Dialog", "CONFIRM PASSWORD"))
        self.finish_btn.setText(_translate("Dialog", "Finish"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "FORGOT PASSWORD"))

    def onclick_login(self):
        username = self.usr_cbox.currentText()
        password = self.pass_box.text()
        verification = validate_user(username, password)

    def onclick_register(self):
        name = self.name_box.text()
        desgination = self.desi_cbox.currentText()
        username = self.rusr_box.text()
        password = self.rpass_box.text()
        c_password = self.concpass_box.text()

        def check():
            if name != "" and username != "" and password != "" and c_password != "":
                return True
            else:
                return False

        if (password == c_password) and check():
            create_new_user(username, password, name, desgination)
            self.name_box.clear()
            self.rusr_box.clear()
            self.concpass_box.clear()
            self.rpass_box.clear()
            self.tabWidget.setCurrentIndex(0)
            self.usr_cbox.addItem(username)

        else:
            pass

    def onclick_forgot_finish(self):
        name = self.fname_box.text()
        username = self.fusrname_box.text()
        new_password = self.fpass_box.text()
        c_password = self.fconcpass_box.text()

        def check():
            if name != "" and username != "" and new_password != "" and c_password != "":
                return True
            else:
                return False

        if (new_password == c_password) and check():
            self.fname_box.clear()
            self.fusrname_box.clear()
            self.fpass_box.clear()
            self.fconcpass_box.clear()
            self.tabWidget.setCurrentIndex(0)
            update_password(username, new_password)
        else:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())