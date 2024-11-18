
# -*- coding: utf-8 -*-
import sys
import os                   #Win Fun's

from PyQt4 import QtCore, QtGui, uic, Qt
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
from datetime import datetime

# 한글 메시지 추가 깨짐 방지---------------------------
reload(sys)
sys.setdefaultencoding('utf-8')
# 한글 메시지 추가 깨짐 방지---------------------------

try:
    if sys.frozen:
        sys.setdefaultencoding("utf-8")
except:
    pass

form_class = uic.loadUiType("Study_Py.ui")[0]
class MyWindow(QMainWindow, form_class):
    #global gReadList(255)

 def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("Study_Python")

# Main Start *****************************************
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

