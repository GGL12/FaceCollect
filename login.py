import cv2
import  pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login_ui import *
from main import *
import os

class Login(QMainWindow, Ui_login):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.enter.clicked.connect(self.enter_d)
        self.exit.clicked.connect(self.exit_d)
        self.account.setPlaceholderText("账号")
        self.word.setEchoMode(QLineEdit.Password)
        self.word.setPlaceholderText("密码")
        logoo1 = QtGui.QPixmap('img\login.jpg')
        self.logoo.setPixmap(logoo1)
        self.num = 0
     
        
    
    def enter_d(self):
        def load_file(file_path):
            pat = []
            with open(file_path,"r+") as f:
                for i in f.readlines():
                    pat.append(i.replace("\n",''))
            return pat
        user = load_file("./login_info/账号.txt")
        password = load_file("./login_info/密码.txt")
        self.id_password = dict(zip(user,password))
   
        '''
        i = 0
        for line1 in id:
            m = i+1
            for line2 in password:
                i = i+1
                if i == m:
                    self.id_password[line1]=line2
                    break
                if i < m:
                    continue
                    #如果输入账号不在账号表文件中，则推送消息框提醒
        '''
        if self.account.text() not in self.id_password.keys():
           self.prompt.setText("账号或密码输入错误") 
           #replay = QMessageBox.warning(self, "!", "账号或密码输入错误", QMessageBox.Yes)
        else:
            if self.id_password[self.account.text()] == self.word.text():
                #账号密码验证成功，创建主界面，进入信息管理程序,并关闭登录窗口
                self.timer = QTimer()
                self.timer.start()
                self.timer.setInterval(100)
                self.timer.timeout.connect(self.show_action)
            else:
                self.prompt.setText("账号或密码输入错误")
                #replay = QMessageBox.warning(self, "!", "账号或密码输入错误", QMessageBox.Yes)
    def exit_d(self):
        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.show_close)
        
    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Escape):
           self.timer = QTimer()
           self.timer.start()
           self.timer.setInterval(100)
           self.timer.timeout.connect(self.show_close)
        if (event.key() == Qt.Key_Enter):
            def load_file(file_path):
                pat = []
                with open(file_path,"r+") as f:
                    for i in f.readlines():
                        pat.append(i.replace("\n",''))
                return pat
            user = load_file("./login_info/账号.txt")
            password = load_file("./loginr_info/密码.txt")
            self.id_password = dict(zip(user,password))
            if self.account.text() not in self.id_password.keys():
               self.prompt.setText("账号或密码输入错误") 
               #replay = QMessageBox.warning(self, "!", "账号或密码输入错误", QMessageBox.Yes)
            else:
                if self.id_password[self.account.text()] == self.word.text():
                    #账号密码验证成功，创建主界面，进入信息管理程序,并关闭登录窗口
                    self.timer = QTimer()
                    self.timer.start()
                    self.timer.setInterval(100)
                    self.timer.timeout.connect(self.show_action)
                else:
                    self.prompt.setText("账号或密码输入错误")
           
    def show_action(self):   
        if self.num == 36 :
            self.shop = MyWindow()
            self.shop.show()
            self.close()
        elif self.num == 0:
            self.prompt.setText("登录成功,加载中·")
        elif self.num == 12:
            self.prompt.setText("登录成功,加载中··")
        elif self.num == 24:
            self.prompt.setText("登录成功,加载中···")
        self.num = self.num + 1 

    def show_close(self):   
        if self.num >36 :
            self.close()
        else:
            self.prompt.setText(str(3 - (self.num // 12))+"S后退出")
        self.num = self.num + 1 
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = Login()
    myWin.show()
    sys.exit(app.exec_())
