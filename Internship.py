import media
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QImage, QPixmap
import requests
import mysql.connector as mc
import sys
import Homepage
import About
import hacks


class Ui_InternshipWindow(object):
    def link(self, linkStr):
        QDesktopServices.openUrl(QUrl(linkStr))
    def HomeCall(self,email,password):
        self.window = QtWidgets.QMainWindow()
        self.ui = Homepage.Ui_HomeWindow()
        self.ui.setupUi(self.window,email,password)
        self.window.show()
    def AboutCall(self,email,password):
        self.window = QtWidgets.QMainWindow()
        self.ui = About.Ui_AboutWindow()
        self.ui.setupUi(self.window,email,password)
        self.window.show()
    def HackCall(self,email,password):
        self.window = QtWidgets.QMainWindow()
        self.ui = hacks.Ui_HackWindow()
        self.ui.setupUi(self.window,email,password)
        self.window.show()
    def setupUi(self, MainWindow,email,password):
        self.email = email
        self.password = password
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(229, 184, 244);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1250, 800))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
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
        mydb = mc.connect(host="localhost", user="root", password="root", database="devhack")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT name FROM user_reg_data WHERE email='{0}' and password='{1}'".format(self.email,self.password))
        self.user_name = (mycursor.fetchone())
        self.user_name = ''.join(self.user_name)     
        # print(self.user_name)  
        self.Hello__User_Name.setText("Hello " + self.user_name)
        self.verticalLayout_4.addWidget(self.Hello__User_Name, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.frame_3)
        spacerItem = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Home_button = QtWidgets.QPushButton(self.frame,clicked = lambda: self.HomeCall(self.email,self.password))
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
        self.Internships_button = QtWidgets.QPushButton(self.frame)
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
        self.About_button = QtWidgets.QPushButton(self.frame, clicked= lambda: self.AboutCall(self.email,self.password))
        self.About_button.clicked.connect(MainWindow.close)
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
"image: url(:/icons/notification_light_purple.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"image: url(:/icons/notification_white.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    image: url(:/icons/notification.png);\n"
"}")
        self.Notifications_button.setText("")
        self.Notifications_button.setShortcut("")
        self.Notifications_button.setAutoDefault(False)
        self.Notifications_button.setDefault(False)
        self.Notifications_button.setFlat(True)
        self.Notifications_button.setObjectName("Notifications_button")
        self.horizontalLayout.addWidget(self.Notifications_button)
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 800))
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1901, 1730))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.poster_area = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.poster_area.setEnabled(True)
        self.poster_area.setMinimumSize(QtCore.QSize(0, 500))
        self.poster_area.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.poster_area.setStyleSheet("background-image: url(:/images/media/MISSION UNICORN BANNER.png);")
        self.poster_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.poster_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.poster_area.setObjectName("poster_area")
        self.verticalLayout_2.addWidget(self.poster_area)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 800))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_2.setLineWidth(1)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1863, 780))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = {}
        mydb = mc.connect(host="localhost", user="root", password="root", database="devhack")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(Internship_id) FROM Internship_data;")
        count = mycursor.fetchone()
        for i in range(1,count[0]+1):                
                self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
                self.frame_8.setMinimumSize(QtCore.QSize(0, 250))
                self.frame_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "border-radius:15px;")
                self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_8.setObjectName("frame_8")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.frame_12 = QtWidgets.QFrame(self.frame_8)
                self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_12.setObjectName("frame_12")
                self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_12)
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                self.label = QtWidgets.QLabel(self.frame_12)
                font = QtGui.QFont()
                font.setFamily("Leelawadee UI")
                font.setPointSize(26)
                font.setBold(True)
                mycursor.execute("SELECT * FROM Internship_data WHERE Internship_Id='%s'" %str(i))
                self.intership_data_fetched = mycursor.fetchone()
                # self.name_of_hack = "".join(self.name_of_hack)
                # print(self.name_of_hack)
                # self.name_of_hack = "Global Hacks Hackathon: 2022 - 2023"
                self.label.setFont(font)
                self.label.setText(str(self.intership_data_fetched[1]))
                self.label.setStyleSheet("color: rgb(45, 3, 59);")
                self.label.setObjectName("label")
                self.verticalLayout_6.addWidget(self.label)
                self.label_3 = QtWidgets.QLabel(self.frame_12)
                font = QtGui.QFont()
                font.setFamily("Leelawadee UI")
                font.setPointSize(16)
                # mycursor.execute("SELECT Start_date FROM hackathons_data WHERE Hack_Id='%s'" %str(i))
                self.label_3.setFont(font)
                self.label_3.setText(self.intership_data_fetched[4])
                self.label_3.setStyleSheet("color: rgb(215, 89, 43);")
                self.label_3.setObjectName("label_3")
                self.verticalLayout_6.addWidget(self.label_3)
                self.label_4 = QtWidgets.QLabel(self.frame_12)
                font = QtGui.QFont()
                font.setFamily("Leelawadee")
                font.setPointSize(12)
                self.label_4.setFont(font)
                # self.name_of_hack[2] = ''.join(self.name_of_hack[2])
                # self.label_4.setText(self.intership_data_fetched[])
                self.label_4.setStyleSheet("color: rgb(142, 144, 161);")
                self.label_4.setObjectName("label_4")
                self.verticalLayout_6.addWidget(self.label_4)
                self.label_5 = QtWidgets.QLabel(self.frame_12)
                font = QtGui.QFont()
                font.setFamily("Leelawadee UI")
                font.setPointSize(16)
                self.label_5.setFont(font)
                self.label_5.linkActivated.connect(self.link)
                self.label_5.setText(self.intership_data_fetched[2])
                self.label_5.setStyleSheet("QLabel{\n"
"color: rgb(45, 3, 59);\n"
"text-align:center;\n"
"}\n"
"QLabel:hover{    \n"
"    color: rgb(255, 0, 0);\n"
"}")
                self.label_5.setObjectName("label_5")
                self.verticalLayout_6.addWidget(self.label_5)
                self.pushButton_8 = QtWidgets.QLabel(self.frame_12)
                self.pushButton_8.setMinimumSize(QtCore.QSize(0, 50))
                font = QtGui.QFont()
                font.setFamily("Leelawadee UI")
                font.setPointSize(16)
                font.setBold(True)
                self.pushButton_8.setFont(font)
                self.pushButton_8.setText('<center><a href="'+self.intership_data_fetched[5]+'"style ="color:white"> Apply</a></center>')
                self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_8.setStyleSheet("background-color: rgb(45, 3, 59);\n"
                "color: rgb(255, 255, 255);")
                self.pushButton_8.linkActivated.connect(self.link)
                self.pushButton_8.setObjectName("pushButton_8")
                self.verticalLayout_6.addWidget(self.pushButton_8)
                self.horizontalLayout_3.addWidget(self.frame_12)
                self.Image_label = QtWidgets.QLabel(self.frame_8)
                self.Image_label.setMinimumSize(QtCore.QSize(500, 0))
                self.Image_label.setText("")
                self.image = QImage()
                self.image.loadFromData(requests.get(self.intership_data_fetched[3]).content)
                self.Image_label.setPixmap(QPixmap(self.image))
                self.Image_label.show()
                self.Image_label.setObjectName("Image_label")
                self.horizontalLayout_3.addWidget(self.Image_label, 0, QtCore.Qt.AlignHCenter)
                self.verticalLayout_5.addWidget(self.frame_8)
                self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
                self.horizontalLayout_2.addWidget(self.scrollArea_2)
                
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_15 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setMinimumSize(QtCore.QSize(1200, 400))
        self.frame_15.setStyleSheet("background-color: rgb(45, 3, 59);\n"
"border-top-right-radius:45px;\n"
"border-top-left-radius:45px;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_22 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(48)
        font.setItalic(False)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_14.addWidget(self.label_22, 0, QtCore.Qt.AlignHCenter)
        self.frame_32 = QtWidgets.QFrame(self.frame_15)
        self.frame_32.setStyleSheet("")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_23 = QtWidgets.QLabel(self.frame_32)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(11)
        font.setBold(True)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_16.addWidget(self.label_23, 0, QtCore.Qt.AlignBottom)
        self.devhack_Email_button = QtWidgets.QPushButton(self.frame_32)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        self.devhack_Email_button.setFont(font)
        self.devhack_Email_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.devhack_Email_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.devhack_Email_button.setObjectName("devhack_Email_button")
        self.verticalLayout_16.addWidget(self.devhack_Email_button, 0, QtCore.Qt.AlignLeft)
        self.label_24 = QtWidgets.QLabel(self.frame_32)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(11)
        font.setBold(True)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_16.addWidget(self.label_24, 0, QtCore.Qt.AlignBottom)
        self.label_25 = QtWidgets.QLabel(self.frame_32)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_16.addWidget(self.label_25, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_14.addWidget(self.frame_32)
        self.frame_33 = QtWidgets.QFrame(self.frame_15)
        self.frame_33.setMinimumSize(QtCore.QSize(300, 300))
        self.frame_33.setStyleSheet("border-top-right-radius:15px;")
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_26 = QtWidgets.QLabel(self.frame_33)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(11)
        font.setBold(True)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_17.addWidget(self.label_26, 0, QtCore.Qt.AlignVCenter)
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_33)
        self.pushButton_27.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_27.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;")
        self.pushButton_27.setText("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.verticalLayout_17.addWidget(self.pushButton_27)
        self.frame_34 = QtWidgets.QFrame(self.frame_33)
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.FB_Devhack = QtWidgets.QPushButton(self.frame_34)
        self.FB_Devhack.setMinimumSize(QtCore.QSize(0, 100))
        self.FB_Devhack.setMaximumSize(QtCore.QSize(100, 16777215))
        self.FB_Devhack.setStyleSheet("image: url(:/icons/media/facebook.png);\n"
"border-radius:50px;")
        self.FB_Devhack.setText("")
        self.FB_Devhack.setObjectName("FB_Devhack")
        self.horizontalLayout_15.addWidget(self.FB_Devhack)
        self.Twitter_Devhack = QtWidgets.QPushButton(self.frame_34)
        self.Twitter_Devhack.setMinimumSize(QtCore.QSize(0, 100))
        self.Twitter_Devhack.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Twitter_Devhack.setStyleSheet("image: url(:/icons/media/twitter.png);\n"
"border-radius:50px;")
        self.Twitter_Devhack.setText("")
        self.Twitter_Devhack.setObjectName("Twitter_Devhack")
        self.horizontalLayout_15.addWidget(self.Twitter_Devhack)
        self.Insta_Devhack = QtWidgets.QPushButton(self.frame_34)
        self.Insta_Devhack.setMinimumSize(QtCore.QSize(0, 100))
        self.Insta_Devhack.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Insta_Devhack.setStyleSheet("image: url(:/icons/media/insta.png);\n"
"border-radius:50px;")
        self.Insta_Devhack.setText("")
        self.Insta_Devhack.setObjectName("Insta_Devhack")
        self.horizontalLayout_15.addWidget(self.Insta_Devhack)
        self.verticalLayout_17.addWidget(self.frame_34)
        self.horizontalLayout_14.addWidget(self.frame_33, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_15)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.User_Icon.setText(_translate("MainWindow", "PushButton"))
        self.DEVHACK.setText(_translate("MainWindow", "DEVHACK"))
        # self.Hello__User_Name.setText(_translate("MainWindow", "HELLO AMBRISH"))
        self.Home_button.setText(_translate("MainWindow", "HOME"))
        self.Hackathons_button.setText(_translate("MainWindow", "  HACKATHONS  "))
        # self.Organize_button.setText(_translate("MainWindow", "  ORGANIZE  "))
        self.Internships_button.setText(_translate("MainWindow", "  INTERNSHIPS  "))
        self.About_button.setText(_translate("MainWindow", "ABOUT"))
        self.label.setText(_translate("MainWindow", "Global Hacks Hackathon: 2022 - 2023"))
        self.label_3.setText(_translate("MainWindow", "Starting date and Ending Date"))
        self.label_4.setText(_translate("MainWindow", "Free"))
        self.label_5.setText(_translate("MainWindow", "Conducting Institution\'s name"))
        self.pushButton_8.setText(_translate("MainWindow", "Apply"))
        self.label_22.setText(_translate("MainWindow", "We love \n"
"software and \n"
"the people who \n"
"build them."))
        self.label_23.setText(_translate("MainWindow", "E-mail"))
        self.devhack_Email_button.setText(_translate("MainWindow", "devhack.community@gmail.com"))
        self.label_24.setText(_translate("MainWindow", "Phone "))
        self.label_25.setText(_translate("MainWindow", "112-95412322563\n"
"111-96452998114\n"
""))
        self.label_26.setText(_translate("MainWindow", "Follow us"))
# import media_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_InternshipWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setWindowTitle("Internship Page")
    sys.exit(app.exec_())
