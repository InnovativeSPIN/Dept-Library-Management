"""
Date started   : 09 Apr 2021
Developers     : MANOJ_KUMAR_S | SARAVANAN_M | HARI_PRASAD_J
"""


import sys
from login_frontend import LoginFrontend
from utils import close_db
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
app.setStyle("fusion")
Dialog = QtWidgets.QDialog()
Dialog.setWindowIcon(QtGui.QIcon("Assets/icon.ico"))
ui = LoginFrontend()
ui.setupUi(Dialog)
Dialog.show()
if not app.exec_():
    close_db()
    sys.exit()
