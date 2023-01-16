import os
import sys
from PyQt5 import QtWidgets,uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFrame, QStackedWidget, QVBoxLayout, QWidget, QFileDialog, QGridLayout


#button-codes-100
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
    
#button-codes-300
class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi("./Login.ui", self)

        self.button301 = self.findChild(QPushButton, "SignIn_button")
        self.button301.clicked.connect(self.home_call)
    def home_call(self):
        screen5 = HomeWindow()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex()+1)

#button-codes-400
class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        uic.loadUi("./Homepage.ui", self)

        self.button401 = self.findChild(QPushButton, "Home_button")
        self.button401.clicked.connect()

        self.button402 = self.findChild(QPushButton, "Hackathons_button")
        self.button402.clicked.connect()

        self.button403 = self.findChild(QPushButton, "Organize_button")
        self.button403.clicked.connect()

        self.button404 = self.findChild(QPushButton, "Internships_button")
        self.button404.clicked.connect()

        self.button405 = self.findChild(QPushButton, "About_button")
        self.button405.clicked.connect()

        self.button406 = self.findChild(QPushButton, "Read_more_button")
        self.button406.clicked.connect()
    

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