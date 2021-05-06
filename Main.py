"""
Date started   : 09 Apr 2021
Developers     : MANOJ_KUMAR_S | SARAVANAN_M | HARI_PRASAD_J
"""

from PyQt5.QtWidgets import QFileDialog

import sys
from PyQt5 import QtWidgets
from login_frontend import LoginFrontend
from utils import close_db

app = QtWidgets.QApplication(sys.argv)
app.setStyle("fusion")
Dialog = QtWidgets.QDialog()


ui = LoginFrontend()
ui.setupUi(Dialog)
Dialog.show()
if not app.exec_():
    close_db()
    sys.exit()
