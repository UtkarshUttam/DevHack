from PyQt5 import QtCore, QtGui, QtWidgets
import Homepage
import hacks
import Internship


class Ui_AboutWindow(object):
    def HackCall(self,email,password):
        self.window = QtWidgets.QMainWindow()
        self.ui = hacks.Ui_HackWindow()
        self.ui.setupUi(self.window,email,password)
        self.window.show()
    def HomeCall(self,email,password):
        self.window = QtWidgets.QMainWindow()
        self.ui = Homepage.Ui_HomeWindow()
        self.ui.setupUi(self.window,email,password)
        self.window.show()
    def InternCall(self,email,password):
        self.window = QtWidgets.QMainWindow()
        self.ui = Internship.Ui_InternshipWindow()
        self.ui.setupUi(self.window,email,password)
        self.window.show()
    def setupUi(self, MainWindow, email, password):
        self.email = email
        self.password = password
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(229, 184, 244);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1250, 800))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.User_Icon = QtWidgets.QPushButton(self.frame)
        self.User_Icon.setMinimumSize(QtCore.QSize(0, 100))
        self.User_Icon.setMaximumSize(QtCore.QSize(100, 16777215))
        self.User_Icon.setStyleSheet("border-radius:50px;\n"
"background-color: rgb(45, 3, 59);\n"
"image: url(:/icons/media/D-logo.png);")
        self.User_Icon.setText("")
        self.User_Icon.setObjectName("User_Icon")
        self.horizontalLayout.addWidget(self.User_Icon)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.DEVHACK = QtWidgets.QLabel(self.frame_3)
        self.DEVHACK.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.DEVHACK.setFont(font)
        self.DEVHACK.setStyleSheet("color: rgb(129, 12, 168);")
        self.DEVHACK.setObjectName("DEVHACK")
        self.verticalLayout_4.addWidget(self.DEVHACK, 0, QtCore.Qt.AlignBottom)
        self.Hello__User_Name = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Hello__User_Name.setFont(font)
        self.Hello__User_Name.setStyleSheet("color: rgb(129, 12, 168);")
        self.Hello__User_Name.setObjectName("Hello__User_Name")
        self.verticalLayout_4.addWidget(self.Hello__User_Name, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Home_button = QtWidgets.QPushButton(self.frame, clicked = lambda: self.HomeCall(self.email,self.password))
        self.Home_button.clicked.connect(MainWindow.close)
        self.Home_button.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Kokila")
        font.setPointSize(20)
        font.setBold(False)
        self.Home_button.setFont(font)
        self.Home_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Home_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(45, 3, 59);\n"
"color: rgb(229, 184, 244);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(182, 12, 238);\n"
"    color: rgb(45, 3, 59);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color: rgb(67, 53, 71);    \n"
"    color: rgb(229, 184, 244);\n"
"}")
        self.Home_button.setObjectName("Home_button")
        self.horizontalLayout.addWidget(self.Home_button)
        self.Hackathons_button = QtWidgets.QPushButton(self.frame, clicked = lambda: self.HackCall(self.email,self.password))
        self.Hackathons_button.clicked.connect(MainWindow.close)
        self.Hackathons_button.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Kokila")
        font.setPointSize(20)
        font.setBold(False)
        self.Hackathons_button.setFont(font)
        self.Hackathons_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Hackathons_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(45, 3, 59);\n"
"color: rgb(229, 184, 244);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(182, 12, 238);\n"
"    color: rgb(45, 3, 59);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color: rgb(67, 53, 71);    \n"
"    color: rgb(229, 184, 244);\n"
"}")
        self.Hackathons_button.setObjectName("Hackathons_button")
        self.horizontalLayout.addWidget(self.Hackathons_button)
#         self.Organize_button = QtWidgets.QPushButton(self.frame)
#         self.Organize_button.setMinimumSize(QtCore.QSize(0, 50))
#         font = QtGui.QFont()
#         font.setFamily("Kokila")
#         font.setPointSize(20)
#         font.setBold(False)
#         self.Organize_button.setFont(font)
#         self.Organize_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.Organize_button.setStyleSheet("QPushButton{\n"
# "background-color: rgb(45, 3, 59);\n"
# "color: rgb(229, 184, 244);\n"
# "border-radius:10px;\n"
# "}\n"
# "\n"
# "QPushButton:hover{    \n"
# "    background-color: rgb(182, 12, 238);\n"
# "    color: rgb(45, 3, 59);\n"
# "}\n"
# "\n"
# "QPushButton:pressed{    \n"
# "    background-color: rgb(67, 53, 71);    \n"
# "    color: rgb(229, 184, 244);\n"
# "}")
#         self.Organize_button.setObjectName("Organize_button")
        # self.horizontalLayout.addWidget(self.Organize_button)
        self.Internships_button = QtWidgets.QPushButton(self.frame, clicked = lambda: self.InternCall(self.email, self.password))
        self.Internships_button.clicked.connect(MainWindow.close)
        self.Internships_button.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Kokila")
        font.setPointSize(20)
        font.setBold(False)
        self.Internships_button.setFont(font)
        self.Internships_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Internships_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(45, 3, 59);\n"
"color: rgb(229, 184, 244);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(182, 12, 238);\n"
"    color: rgb(45, 3, 59);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color: rgb(67, 53, 71);    \n"
"    color: rgb(229, 184, 244);\n"
"}")
        self.Internships_button.setObjectName("Internships_button")
        self.horizontalLayout.addWidget(self.Internships_button)
        self.About_button = QtWidgets.QPushButton(self.frame)
        self.About_button.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Kokila")
        font.setPointSize(20)
        font.setBold(False)
        self.About_button.setFont(font)
        self.About_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.About_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(45, 3, 59);\n"
"color: rgb(229, 184, 244);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(182, 12, 238);\n"
"    color: rgb(45, 3, 59);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color: rgb(67, 53, 71);    \n"
"    color: rgb(229, 184, 244);\n"
"}")
        self.About_button.setObjectName("About_button")
        self.horizontalLayout.addWidget(self.About_button)
        self.Notifications_button = QtWidgets.QPushButton(self.frame)
        self.Notifications_button.setMinimumSize(QtCore.QSize(0, 70))
        self.Notifications_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Notifications_button.setStyleSheet("QPushButton{\n"
"    image: url(:/icons/media/notification_light_purple.png);\n"
"    border:None;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    image: url(:/icons/media/notification_white.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    image: url(:/icons/media/notification.png);\n"
"}")
        self.Notifications_button.setText("")
        self.Notifications_button.setShortcut("")
        self.Notifications_button.setAutoDefault(False)
        self.Notifications_button.setDefault(False)
        self.Notifications_button.setFlat(True)
        self.Notifications_button.setObjectName("Notifications_button")
        self.horizontalLayout.addWidget(self.Notifications_button)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.0568182, stop:0 rgba(45, 3, 59, 255), stop:1 rgba(129, 12, 168, 255));\n"
"border-radius:50px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setStyleSheet("background:transparent;\n"
"image: url(:/icons/media/white_logo.png);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DEVHACK.setText(_translate("MainWindow", "DEVHACK"))
        self.Hello__User_Name.setText(_translate("MainWindow", "HELLO AMBRISH"))
        self.Home_button.setText(_translate("MainWindow", "HOME"))
        self.Hackathons_button.setText(_translate("MainWindow", "  HACKATHONS  "))
        # self.Organize_button.setText(_translate("MainWindow", "  ORGANIZE  "))
        self.Internships_button.setText(_translate("MainWindow", "  INTERNSHIPS  "))
        self.About_button.setText(_translate("MainWindow", "ABOUT"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Welcome to DEVHACK, your one-stop platform for hackathons and internships. Our aim is to provide developers, designers, and engineers with a convenient </span></p><p><span style=\" font-size:20pt;\">and efficient way to discover and apply to the latest opportunities in the tech industry.</span></p><p><span style=\" font-size:20pt;\">With DEVHACK, you can easily browse through a vast database of hackathons and internships, filtered by location, skills, and industry. Whether you\'re a </span></p><p><span style=\" font-size:20pt;\">seasoned veteran or just starting out, our platform offers a wide range of options to match your skills and interests.</span></p><p><span style=\" font-size:20pt;\">One of the key features of DEVHACK is our application management system. We understand that applying to hackathons and internships can be </span></p><p><span style=\" font-size:20pt;\">time-consuming, so we\'ve made the process as seamless as possible. You can manage your applications, receive notifications, and even track your progress </span></p><p><span style=\" font-size:20pt;\">directly from our platform.</span></p><p><span style=\" font-size:20pt;\">We are committed to helping you grow your skills and advance your career, and we believe that participating in hackathons and internships is one of the best </span></p><p><span style=\" font-size:20pt;\">ways to do so. That\'s why we\'ve built DEVHACK to make it easier for you to find and apply to these opportunities.</span></p><p><span style=\" font-size:20pt;\">So if you\'re ready to take your skills to the next level, join us on DEVHACK and start exploring the world of hackathons and internships today!</span></p></body></html>"))
# import media_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AboutWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setWindowTitle("About Page")
    sys.exit(app.exec_())
