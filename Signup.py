from PyQt5 import QtCore, QtGui, QtWidgets
import Login
from PyQt5.QtWidgets import *
import mysql.connector as mc
import sys
import media

class Ui_SignupWindow(QMainWindow):
    def Logincall(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Login.Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def reg_action(self,name,mobile,email,pass1,pass2):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.pass1 = pass1
        self.pass2 = pass2
        if (self.pass1 == self.pass2):
            mydb = mc.connect(host="localhost", user="root", password="root", database="devhack")
            mycursor = mydb.cursor()
            query = "INSERT INTO user_reg_data(name,mobile,email,password) values(%s,%s,%s,%s)"
            value = (self.name,self.mobile,self.email,self.pass1)
            try:
                mycursor.execute(query, value)
                mydb.commit()
                QMessageBox.about(self,"Sucess!","Data Inserted")
                self.Logincall()
            except:
                QMessageBox.about(self,"Sorry!","Data didn't Inserted")
        else:
            QMessageBox.about(self,"Error!","Passwords don't match")
    def setupUi(self, SignupWindow):
        SignupWindow.setObjectName("SignupWindow")
        SignupWindow.resize(1920, 1080)
        SignupWindow.setMinimumSize(QtCore.QSize(1500, 800))
        SignupWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.0568182, stop:0.204545 rgba(180, 100, 206, 255), stop:1 rgba(94, 53, 108, 255));")
        self.centralwidget = QtWidgets.QWidget(SignupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(700, 0))
        self.frame.setStyleSheet("background:transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(40)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_10.setStyleSheet("background-image: url(:/images/media/sign_up_2.jpg);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4.addWidget(self.frame_10)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(48)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(4, 49, 51);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setMinimumSize(QtCore.QSize(300, 0))
        self.label_6.setStyleSheet("image: url(:/icons/media/Color logo black - no background.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(77, 89, 89);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.name_entry = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_entry.sizePolicy().hasHeightForWidth())
        self.name_entry.setSizePolicy(sizePolicy)
        self.name_entry.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.name_entry.setFont(font)
        self.name_entry.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(182, 183, 184);\n"
"}\n"
"\n"
"QLineEdit:Focus{\n"
"background-color: rgb(239, 240, 242);\n"
"}")
        self.name_entry.setInputMask("")
        self.name_entry.setFrame(False)
        self.name_entry.setObjectName("name_entry")
        self.verticalLayout_2.addWidget(self.name_entry)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(77, 89, 89);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.email_entry = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_entry.sizePolicy().hasHeightForWidth())
        self.email_entry.setSizePolicy(sizePolicy)
        self.email_entry.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.email_entry.setFont(font)
        self.email_entry.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(182, 183, 184);\n"
"}\n"
"\n"
"QLineEdit:Focus{\n"
"background-color: rgb(239, 240, 242);\n"
"}")
        self.email_entry.setFrame(False)
        self.email_entry.setObjectName("email_entry")
        self.verticalLayout_2.addWidget(self.email_entry)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(77, 89, 89);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.mobile_entry = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mobile_entry.sizePolicy().hasHeightForWidth())
        self.mobile_entry.setSizePolicy(sizePolicy)
        self.mobile_entry.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.mobile_entry.setFont(font)
        self.mobile_entry.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(182, 183, 184);\n"
"}\n"
"\n"
"QLineEdit:Focus{\n"
"background-color: rgb(239, 240, 242);\n"
"}")
        self.mobile_entry.setInputMask("")
        self.mobile_entry.setFrame(False)
        self.mobile_entry.setObjectName("mobile_entry")
        self.verticalLayout_2.addWidget(self.mobile_entry)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(77, 89, 89);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.password_1 = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_1.sizePolicy().hasHeightForWidth())
        self.password_1.setSizePolicy(sizePolicy)
        self.password_1.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.password_1.setFont(font)
        self.password_1.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(182, 183, 184);\n"
"}\n"
"\n"
"QLineEdit:Focus{\n"
"background-color: rgb(239, 240, 242);\n"
"}")
        self.password_1.setFrame(False)
        self.password_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_1.setObjectName("password_1")
        self.verticalLayout_2.addWidget(self.password_1)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(77, 89, 89);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.password_2 = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_2.sizePolicy().hasHeightForWidth())
        self.password_2.setSizePolicy(sizePolicy)
        self.password_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.password_2.setFont(font)
        self.password_2.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(182, 183, 184);\n"
"}\n"
"\n"
"QLineEdit:Focus{\n"
"background-color: rgb(239, 240, 242);\n"
"}")
        self.password_2.setFrame(False)
        self.password_2.setObjectName("password_2")
        self.verticalLayout_2.addWidget(self.password_2)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Submit_button = QtWidgets.QPushButton(self.frame_5, clicked = lambda: self.reg_action(self.name_entry.text(),self.mobile_entry.text(),self.email_entry.text(),self.password_1.text(),self.password_2.text()))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Submit_button.sizePolicy().hasHeightForWidth())
        self.Submit_button.setSizePolicy(sizePolicy)
        self.Submit_button.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(26)
        self.Submit_button.setFont(font)
        self.Submit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Submit_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 112, 116);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 112, 116);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 59, 61);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Submit_button.setObjectName("Submit_button")
        self.verticalLayout_3.addWidget(self.Submit_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(77, 89, 89);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9, 0, QtCore.Qt.AlignRight)
        self.Log_in_pushbutton = QtWidgets.QPushButton(self.frame_7, clicked = lambda: self.Logincall())
        self.Log_in_pushbutton.clicked.connect(SignupWindow.close)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(True)
        self.Log_in_pushbutton.setFont(font)
        self.Log_in_pushbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Log_in_pushbutton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 112, 116);\n"
"border:None;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color:rgb(226, 151, 0)\n"
"}")
        self.Log_in_pushbutton.setFlat(True)
        self.Log_in_pushbutton.setObjectName("Log_in_pushbutton")
        self.horizontalLayout_3.addWidget(self.Log_in_pushbutton, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_3.addWidget(self.frame_7, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_2)
        SignupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignupWindow)
        QtCore.QMetaObject.connectSlotsByName(SignupWindow)

    def retranslateUi(self, SignupWindow):
        _translate = QtCore.QCoreApplication.translate
        SignupWindow.setWindowTitle(_translate("SignupWindow", "MainWindow"))
        self.label_7.setText(_translate("SignupWindow", "The Home for Hackathons \n"
"Internships & Many More"))
        self.label_5.setText(_translate("SignupWindow", "<html><head/><body><p align=\"right\">Welcome to</p></body></html>"))
        self.label.setText(_translate("SignupWindow", "Full Name"))
        self.name_entry.setPlaceholderText(_translate("SignupWindow", "    Enter your name"))
        self.label_2.setText(_translate("SignupWindow", "Email"))
        self.email_entry.setPlaceholderText(_translate("SignupWindow", "   Enter your Email here"))
        self.label_8.setText(_translate("SignupWindow", "Mobile No."))
        self.mobile_entry.setPlaceholderText(_translate("SignupWindow", "    Enter your mobile number"))
        self.label_3.setText(_translate("SignupWindow", "Password"))
        self.password_1.setPlaceholderText(_translate("SignupWindow", "   Enter your Password"))
        self.label_4.setText(_translate("SignupWindow", "Confirm Password"))
        self.password_2.setPlaceholderText(_translate("SignupWindow", "   Re-enter Password"))
        self.Submit_button.setText(_translate("SignupWindow", "    Create Account    "))
        self.label_9.setText(_translate("SignupWindow", "Already have an account?"))
        self.Log_in_pushbutton.setText(_translate("SignupWindow", "Log in"))
# import media_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignupWindow = QtWidgets.QMainWindow()
    ui = Ui_SignupWindow()
    ui.setupUi(SignupWindow)
    SignupWindow.show()
    SignupWindow.setWindowTitle("Signup Page")
    sys.exit(app.exec_())
