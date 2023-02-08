from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Ui_LoginWindow
from Signup import Ui_SignupWindow
import media




class Ui_StartWindow(object):
    def Logincall(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def Regcall(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SignupWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1500, 800))
        MainWindow.setStyleSheet("background-color: rgb(180, 100, 206);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_7.setStyleSheet("image: url(:/icons/media/white_logo.png);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3.addWidget(self.frame_7, 0, QtCore.Qt.AlignLeft)
        self.Login_button = QtWidgets.QPushButton(self.frame_5, clicked = lambda: self.Logincall())
        self.Login_button.clicked.connect(MainWindow.close)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.Login_button.setFont(font)
        self.Login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Login_button.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border:None;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(129, 12, 168);\n"
"}")
        self.Login_button.setFlat(True)
        self.Login_button.setObjectName("Login_button")
        self.horizontalLayout_3.addWidget(self.Login_button)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(30, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(70)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.Get_Started_button = QtWidgets.QPushButton(self.frame_3, clicked = lambda: self.Regcall())
        self.Get_Started_button.setMinimumSize(QtCore.QSize(0, 100))
        self.Get_Started_button.clicked.connect(MainWindow.close)
        self.Get_Started_button.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(36)
        font.setBold(False)
        self.Get_Started_button.setFont(font)
        self.Get_Started_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Get_Started_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(129, 12, 168);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(129, 12, 168);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(69, 6, 90);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.Get_Started_button.setObjectName("Get_Started_button")
        self.verticalLayout_2.addWidget(self.Get_Started_button)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_2.addWidget(self.frame_9)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("image: url(:/images/White_dot_pattern.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setStyleSheet("background:transparent;\n"
"image:None;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout.addWidget(self.frame_10, 0, 3, 1, 1)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setStyleSheet("background:transparent;\n"
"image:None;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout.addWidget(self.frame_11, 1, 0, 1, 1)
        self.frame_13 = QtWidgets.QFrame(self.frame_4)
        self.frame_13.setStyleSheet("background:transparent;\n"
"image:None;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout.addWidget(self.frame_13, 3, 3, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setStyleSheet("/*background:transparent;*/\n"
"image: url(:/images/How-do-hackathons-work.png);\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout.addWidget(self.frame_8, 0, 0, 1, 3)
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setStyleSheet("/*background:transparent;*/\n"
"background-color: rgb(255, 170, 0);\n"
"image:None;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout.addWidget(self.frame_14, 1, 1, 1, 3)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setStyleSheet("/*background:transparent;*/\n"
"background-color: rgb(255, 170, 0);\n"
"image:None;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout.addWidget(self.frame_12, 3, 0, 1, 3)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Login_button.setText(_translate("MainWindow", "Log in"))
        self.label.setText(_translate("MainWindow", "The Home for \n"
"Hackathons \n"
"Internships & \n"
"Many More"))
        self.label_2.setText(_translate("MainWindow", "We speak, we listen, we discuss, \n"
"we grow."))
        self.Get_Started_button.setText(_translate("MainWindow", "Get Started →"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
