# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_help_hh(object):
    def setupUi(self, help_hh):
        help_hh.setObjectName("help_hh")
        help_hh.resize(1150, 850)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        help_hh.setFont(font)
        self.setWindowOpacity(0.85)
        self.centralwidget = QtWidgets.QWidget(help_hh)
        self.centralwidget.setObjectName("centralwidget")
        self.help = QtWidgets.QLabel(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(390, 260, 500, 300))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(19)
        self.help.setFont(font)
        self.help.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.help.setObjectName("help")
        self.bgcolor = QtWidgets.QLabel(self.centralwidget)
        self.bgcolor.setGeometry(QtCore.QRect(0, 0, 1150, 850))
        self.bgcolor.setText("")
        self.bgcolor.setObjectName("bgcolor")
        self.hint = QtWidgets.QLabel(self.centralwidget)
        self.hint.setGeometry(QtCore.QRect(500, 50, 291, 101))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        #self.hint.setFont(font)
        #self.hint.setObjectName("hint")
        self.bgcolor.raise_()
        self.help.raise_()
        #self.hint.raise_()
        help_hh.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(help_hh)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 26))
        self.menubar.setObjectName("menubar")
        help_hh.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(help_hh)
        self.statusbar.setObjectName("statusbar")
        help_hh.setStatusBar(self.statusbar)

        self.retranslateUi(help_hh)
        QtCore.QMetaObject.connectSlotsByName(help_hh)
        
    def retranslateUi(self, help_hh):
        _translate = QtCore.QCoreApplication.translate
        help_hh.setWindowTitle(_translate("help_hh", "帮助"))
        self.help.setText(_translate("help_hh", "信息采集提示\n"
"1.请先打开采集班级的信息表\n"
"2.确定采集人姓名\n"
"3.打开摄像头\n"
"4.关闭摄像头"))
        #self.hint.setText(_translate("help_hh", "帮助中心"))
        
