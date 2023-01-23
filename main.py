import os
import sys
from PyQt5 import QtWidgets,uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import mysql.connector as mc
from store import *



#button-codes-100
#button100 --> Get started button

class StartingWindow(QMainWindow):
    def __init__(self):
        super(StartingWindow,self).__init__()
        uic.loadUi("./Starting_Page.ui",self)
        
        self.button100 = self.findChild(QPushButton, "Get_Started_button")
        self.button100.clicked.connect(self.register_call)

        self.button101 = self.findChild(QPushButton, "Login_button")
        self.button101.clicked.connect(self.login_call)        

    def register_call(self):
        screen2 = RegisterWindow()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def login_call(self):
        screen4 = LoginWindow()
        widget.addWidget(screen4)
        widget.setCurrentIndex(widget.currentIndex()+1)

#button-codes-200
class RegisterWindow(QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        uic.loadUi("./Signup.ui", self)

        self.button201 = self.findChild(QPushButton, "Submit_button")
        self.button201.clicked.connect(self.reg_action)
    
    def reg_action(self):
        self.name = self.findChild(QLineEdit, "name_entry").text()
        self.mobile = self.findChild(QLineEdit, "mobile_entry").text()
        self.email = self.findChild(QLineEdit, "email_entry").text()
        self.pass1 = self.findChild(QLineEdit, "password_1").text()
        self.pass2 = self.findChild(QLineEdit, "password_2").text()
        if (self.pass1 == self.pass2):
            mydb = mc.connect(host="localhost", user="root", password="root", database="devhack")
            mycursor = mydb.cursor()
            value = (self.name,self.mobile,self.email,self.pass1)
            query = "INSERT INTO user_reg_data(name,mobile,email,password) values(%s,%s,%s,%s)"
            # try:
            if 1==1:
                if mobilelen(self.mobile) == "True":
                    if passlen(self.pass1) == "True":
                        if mobilereg(self.mobile)== "True":
                            mycursor.execute(query, value)
                            mydb.commit()
                            self.homi_call()
                            QMessageBox.about(self,"Message!","Hellow {0} You have registred successfully".format((self.name).capitalize()))
                        else:
                            QMessageBox.about(self,"Error!","Numbre already registred")
                    else:
                        QMessageBox.about(self,"Error!","Your password must be more than 8 charecter")
                else:
                    QMessageBox.about(self,"Error!","Invalid number")
            else:
                pass
        else:
            QMessageBox.about(self,"Error!","Passwords don't match")
    def homi_call(self):
        screen5 = HomeWindow(self.email,self.pass1)
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)

#button-codes-300
class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi("./Login.ui", self)

        self.button301 = self.findChild(QPushButton, "SignIn_button")
        self.button301.clicked.connect(self.check_credentials)

        self.button302 = self.findChild(QPushButton, "signup_button")
        self.button302.clicked.connect(self.register_call)
    def check_credentials(self):
        self.email = self.findChild(QLineEdit, "email_entry").text()
        self.password = self.findChild(QLineEdit,"password_entry").text()
        if(self.email == ""):
            QMessageBox.about(self,"Invalid entry!","Please enter your email .")
        elif (self.password == ""):
            QMessageBox.about(self,"Invalid entry!","Please enter your password.")
        else:
            if checker(self.email,self.password) == True:
                self.home_call()
            else:
                QMessageBox.about(self,"Error!","Password and email doesn't match")
    def register_call(self):
        screen2 = RegisterWindow()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def home_call(self):
        screen5 = HomeWindow(self.email,self.password)
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)

#button-codes-400
class HomeWindow(QMainWindow):
    def __init__(self,user_email,user_password):
        super(HomeWindow, self).__init__()
        uic.loadUi("./Homepage.ui", self)

        # self.button401 = self.findChild(QPushButton, "Home_button")
        # self.button401.clicked.connect()

        # self.button402 = self.findChild(QPushButton, "Hackathons_button")
        # self.button402.clicked.connect()

        # self.button403 = self.findChild(QPushButton, "Organize_button")
        # self.button403.clicked.connect()

        # self.button404 = self.findChild(QPushButton, "Internships_button")
        # self.button404.clicked.connect()

        # self.button405 = self.findChild(QPushButton, "About_button")
        # self.button405.clicked.connect()

        # self.button406 = self.findChild(QPushButton, "Read_more_button")
        # self.button406.clicked.connect()

        mydb = mc.connect(host="localhost", user="root", password="root", database="devhack")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT name FROM user_reg_data WHERE email='{0}' and password='{1}'".format(user_email,user_password))
        self.user_name = (mycursor.fetchone())
        self.user_name = ''.join(self.user_name)
       
        self.hello_username = self.findChild(QLabel, "Hello__User_Name")
        self.hello_username.setText("Hello "+self.user_name)

#driver-code
app = QApplication(sys.argv)
widget = QStackedWidget()
mainwindow = StartingWindow()
widget.addWidget(mainwindow)
widget.setWindowTitle("DevHack")
widget.setWindowIcon(QtGui.QIcon("./Media/icon.png"))
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting...")