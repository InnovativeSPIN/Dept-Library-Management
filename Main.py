"""
Date started   : 09 Apr 2021
Authors        : MANOJ_KUMAR_S | SARAVANAN_M | HARI_PRASAD_J
"""
from utils import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from login_frontend import Ui_Dialog

app = QtWidgets.QApplication(sys.argv)
app.setStyle("fusion")
Dialog = QtWidgets.QDialog()

ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
