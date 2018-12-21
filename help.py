import sys
from PyQt5 import QtCore, QtGui, uic,QtWidgets
import os
import cv2
import time
import  pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow
from help_ui import *

class help_hh(QMainWindow, Ui_help_hh):
    def __init__(self, parent=None):
        super(help_hh, self).__init__(parent)
        self.setupUi(self)
        bg = QtGui.QPixmap('img\help.jpg')
        self.bgcolor.setPixmap(bg)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    hh = help_hh()
    hh.show()
    sys.exit(app.exec_())
    