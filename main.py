# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 11:45:58 2018

@author: Administrator
"""
import sys
import cv2
import  pandas as pd
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication
from main_ui import *
from help import *
from login import *
import os

class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.open.clicked.connect(self.open_cap)
        self.close_.clicked.connect(self.close_cap)
        self.dete.clicked.connect(self.create_file)
        self.help.clicked.connect(self.help_d)
        self.openfile.clicked.connect(self.open_file)
        self.logout.clicked.connect(self.logout_d)
        #header = QtGui.QPixmap('img\header.jpg')
        #self.header.setPixmap(header)
        #self.label.setStyleSheet("borsder:2px solid black;")
        #boder = QtGui.QPixmap('img\logo2.jpg')
        #self.boder.setPixmap(boder)
        bg = QtGui.QPixmap('img\main.jpg')
        self.bgcolor.setPixmap(bg)
        #self.bgcolor.setStyleSheet("background-color:#ffffff;")
        self.label_2.setStyleSheet("border:2px solid red;")
        #logo1 = QtGui.QPixmap('img\logo1.jpg')
        #self.logo1.setPixmap(logo1)
        self.num = 1
        self.index = 0
        self.count = 0
        
    def open_cap(self):
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.show_image)
        
    def show_image(self):   
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))
        if self.num >59 :
            self.countdown.setText("开始采集")
            if self.num % 6  == 0 and self.count != 20 :
                image_num = self.num // 6 - 9
                file_path = self.root_file + '{:03}.jpg'.format(image_num)
                cv2.imwrite(file_path,self.image)
                self.count = self.count + 1
        else:
            self.countdown.setText(str(5 - (self.num // 12)))
        self.num = self.num + 1 
        
    def create_file(self):
        self.root_file = os.path.split(os.path.realpath(__file__))[0] + "\\collected_image" +'\\' + str(self.class_info.id[self.index]) + '\\'
        if os.path.exists(self.root_file):
            os.remove(self.root_file)
        os.makedirs(self.root_file)
        self.index = self.index + 1
        
    def close_cap(self):
        self.num = 1
        self.timer.stop()
        self.cap.release()
        self.label.clear()
        self.label.setText( "人脸采集区域")
        self.countdown.setText("采集等待中")
        self.text.setText("")
        self.text.setText(self.class_info.name[self.index])
        photo = QtGui.QPixmap(self.absolute_path + '/image/' + str(self.class_info.id[self.index]) + '.jpg')
        self.label_2.setPixmap(photo)
        
    def open_file(self):
        self.absolute_path = QFileDialog.getExistingDirectory(self,"选取文件夹", "/")#(self,'open file', '/')
        #resize photo
        #self.text.setText(str(self.absolute_path))
        
        image_path = self.absolute_path + '/image/'
        for root, dirs, files in os.walk(image_path):
            for photo_file in files:
                photo_path = image_path + photo_file
                image = cv2.imread(photo_path)
                image = cv2.resize(image,(90,120))
                cv2.imwrite(photo_path,image)
        info = self.absolute_path + '/information.xls'
        self.class_info = pd.read_excel(info,header=None,names=['name','id'])
        self.class_dict = dict(zip(self.class_info.id.astype('str'),self.class_info.name))
        self.text.setText(self.class_info.name[self.index])
        photo = QtGui.QPixmap(self.absolute_path + '/image/' + str(self.class_info.id[self.index]) + '.jpg')
        self.label_2.setPixmap(photo)
		
    def help_d(self):
        self.shop = help_hh()
        self.shop.show()

    def logout_d(self):
        self.logout = Login()
        self.logout.show()
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

