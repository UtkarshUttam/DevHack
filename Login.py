import sys
from PyQt5 import QtWidgets,uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import mysql.connector as mc
from PyQt5 import QtCore, QtGui, QtWidgets
from Homepage import Ui_HomeWindow
import media
from xl_sql import scrap_inserter,scrap_inserter2
import Signup


class Ui_LoginWindow(object):
    def HomeCall(self,email,password):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self.window,email,password)
        self.window.show()
    def Regcall(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Signup.Ui_SignupWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def check_credentials(self,email,password):
        self.email = email
        self.password = password
        if(self.email == ""):
            QMessageBox.about(self,"Invalid entry!","Please enter your email .")
        elif (self.password == ""):
            QMessageBox.about(self,"Invalid entry!","Please enter your password.")
        else:
            scrap_inserter()
            scrap_inserter2()
            mydb = mc.connect(host="localhost", user="root", password="root", database="devhack")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT password FROM user_reg_data WHERE email='%s'"%self.email)
            self.fetched_password = mycursor.fetchone()
            self.fetched_password = ''.join(self.fetched_password)
            # mydb.commit()
            if(self.fetched_password == self.password):
                self.HomeCall(self.email,self.password)
            else:
                QMessageBox.about(self,"Error!","Password and email doesn't match")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1500, 800))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(600, 0))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.0568182, stop:0.204545 rgba(180, 100, 206, 255), stop:1 rgba(94, 53, 108, 255));\n"
"border-top-left-radius:52px;\n"
"border-bottom-left-radius:52px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(350, 150))
        self.label.setStyleSheet("background:None;\n"
"image: url(:/icons/media/white_logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(0, 500))
        self.label_2.setStyleSheet("background:None;\n"
"image: url(:/images/media/Login_page_design1.py.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(40)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:None;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-right-radius:52px;\n"
"border-bottom-right-radius:52px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(35, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(36)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignBottom)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(95, 95, 95);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5, 0, QtCore.Qt.AlignBottom)
        self.email_entry = QtWidgets.QLineEdit(self.frame_2)
        self.email_entry.setMinimumSize(QtCore.QSize(600, 65))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.email_entry.setFont(font)
        self.email_entry.setStyleSheet("QLineEdit{\n"
"background-color: rgb(166, 167, 168);\n"
"color: rgb(239, 240, 242);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"color: rgb(119, 120, 121);\n"
"background-color: rgb(239, 240, 242);\n"
"}")
        self.email_entry.setObjectName("email_entry")
        self.verticalLayout_2.addWidget(self.email_entry, 0, QtCore.Qt.AlignLeft)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(95, 95, 95);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6, 0, QtCore.Qt.AlignBottom)
        self.password_entry = QtWidgets.QLineEdit(self.frame_2)
        self.password_entry.setMinimumSize(QtCore.QSize(600, 65))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.password_entry.setFont(font)
        self.password_entry.setStyleSheet("QLineEdit{\n"
"background-color: rgb(166, 167, 168);\n"
"color: rgb(239, 240, 242);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"color: rgb(119, 120, 121);\n"
"background-color: rgb(239, 240, 242);\n"
"}")
        self.password_entry.setInputMask("")
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_entry.setObjectName("password_entry")
        self.verticalLayout_2.addWidget(self.password_entry, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(16)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(95, 95, 95);")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox, 0, QtCore.Qt.AlignTop)
        self.SignIn_button = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.check_credentials(self.email_entry.text(),self.password_entry.text()))
        self.SignIn_button.clicked.connect(MainWindow.close)
        self.SignIn_button.setMinimumSize(QtCore.QSize(488, 52))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(24)
        self.SignIn_button.setFont(font)
        self.SignIn_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SignIn_button.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.0568182, stop:0.204545 rgba(180, 100, 206, 255), stop:1 rgba(94, 53, 108, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"color:rgb(179, 100, 205);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(95, 53, 109);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.SignIn_button.setObjectName("SignIn_button")
        self.verticalLayout_2.addWidget(self.SignIn_button, 0, QtCore.Qt.AlignLeft)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(36, 36, 36);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7, 0, QtCore.Qt.AlignRight)
        self.signup_button = QtWidgets.QPushButton(self.frame_3, clicked = lambda: self.Regcall())
        self.signup_button.clicked.connect(MainWindow.close)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(16)
        self.signup_button.setFont(font)
        self.signup_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signup_button.setStyleSheet("color: rgb(0, 126, 148);")
        self.signup_button.setObjectName("signup_button")
        self.horizontalLayout_2.addWidget(self.signup_button, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "We speak, we listen, \n"
"we discuss, we grow."))
        self.label_4.setText(_translate("MainWindow", "Login to your Account"))
        self.label_5.setText(_translate("MainWindow", "EMAIL"))
        self.email_entry.setPlaceholderText(_translate("MainWindow", "    Enter your email"))
        self.label_6.setText(_translate("MainWindow", "PASSWORD"))
        self.password_entry.setPlaceholderText(_translate("MainWindow", "    Password"))
        self.checkBox.setText(_translate("MainWindow", "REMEMBER ME"))
        self.SignIn_button.setText(_translate("MainWindow", "SIGN IN"))
        self.label_7.setText(_translate("MainWindow", "Don’t have an account?"))
        self.signup_button.setText(_translate("MainWindow", "Sign Up "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setWindowTitle("Login Page")
    sys.exit(app.exec_())
