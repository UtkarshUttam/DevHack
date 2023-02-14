from PyQt5 import QtCore, QtGui, QtWidgets
import hacks
import Internship
import About
import mysql.connector as mc
import media
import webbrowser

class Ui_HomeWindow(object):
    def HackCall(self,email,password):
        self.window = QtWidgets.QMainWindow()
        self.ui = hacks.Ui_HackWindow()
        self.ui.setupUi(self.window,email,password)
        self.window.show()
    def AboutCall(self,email,password):
        self.window = QtWidgets.QMainWindow()
        self.ui = About.Ui_AboutWindow()
        self.ui.setupUi(self.window,email,password)
        self.window.show()
    def InternCall(self,email,password):
        self.window = QtWidgets.QMainWindow()
        self.ui = Internship.Ui_InternshipWindow()
        self.ui.setupUi(self.window,email,password)
        self.window.show()
    def insta_call(self,name):
        if name == 'Utkarsh':
                self.url= 'https://www.instagram.com/utkarshuttam_3/'
        elif name == 'Om':
                self.url = 'https://www.instagram.com/paithankarom/'
        elif name == 'Ambrish':
                self.url = 'https://www.instagram.com/ambrishk.rai/'
        elif name == 'Abhishek':
                self.url = 'https://www.instagram.com/e_m_p_t_y.y/'
        webbrowser.open_new_tab(self.url)
    def linkedin_call(self,name):
        if name == 'Utkarsh':
                self.url= 'https://www.linkedin.com/in/utkarsh-uttam-0884ab1b7/'
        elif name == 'Om':
                self.url = 'https://www.linkedin.com/in/om-paithankar-8180a122a/'
        elif name == 'Ambrish':
                self.url = 'https://www.linkedin.com/in/ambrish-kumar-rai-aa257122b/'
        elif name == 'Abhishek':
                self.url = 'https://www.linkedin.com/in/abhishek-m-973046243/'
        webbrowser.open_new_tab(self.url)
    def github_call(self,name):
        if name == 'Utkarsh':
                self.url= 'https://github.com/UtkarshUttam'
        elif name == 'Om':
                self.url = 'https://github.com/am-i-op'
        elif name == 'Ambrish':
                self.url = 'https://github.com/AmbrishKumarRai'
        elif name == 'Abhishek':
                self.url = 'https://github.com/EMPTY2126'
        webbrowser.open_new_tab(self.url)
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
        self.horizontalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Home_button = QtWidgets.QPushButton(self.frame)
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
        self.Hackathons_button = QtWidgets.QPushButton(self.frame , clicked = lambda: self.HackCall(self.email,self.password))
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
        # self.Organize_button = QtWidgets.QPushButton(self.frame)
        # self.Organize_button.setMinimumSize(QtCore.QSize(0, 50))
        # font = QtGui.QFont()
        # font.setFamily("Kokila")
        # font.setPointSize(20)
        # font.setBold(False)
        # self.Organize_button.setFont(font)
        # self.Organize_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        # self.Organize_button.setObjectName("Organize_button")
        # self.horizontalLayout.addWidget(self.Organize_button)
        self.Internships_button = QtWidgets.QPushButton(self.frame, clicked = lambda: self.InternCall(self.email,self.password))
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
        self.About_button = QtWidgets.QPushButton(self.frame, clicked = lambda: self.AboutCall(self.email,self.password))
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
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -1533, 1901, 3036))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 1400))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.poster_area = QtWidgets.QFrame(self.frame_2)
        self.poster_area.setEnabled(True)
        self.poster_area.setMinimumSize(QtCore.QSize(0, 500))
        self.poster_area.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.poster_area.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-image: url(:/images/media/sliderbannerM32.jpg);")
        self.poster_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.poster_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.poster_area.setObjectName("poster_area")
        self.verticalLayout_2.addWidget(self.poster_area)
        self.Hackathons_and_Internship_area = QtWidgets.QFrame(self.frame_2)
        self.Hackathons_and_Internship_area.setMinimumSize(QtCore.QSize(0, 0))
        self.Hackathons_and_Internship_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Hackathons_and_Internship_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Hackathons_and_Internship_area.setObjectName("Hackathons_and_Internship_area")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Hackathons_and_Internship_area)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Upcoming_hackathons_heading_area = QtWidgets.QFrame(self.Hackathons_and_Internship_area)
        self.Upcoming_hackathons_heading_area.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Upcoming_hackathons_heading_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Upcoming_hackathons_heading_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Upcoming_hackathons_heading_area.setObjectName("Upcoming_hackathons_heading_area")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Upcoming_hackathons_heading_area)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Upcoming_hackathons = QtWidgets.QLabel(self.Upcoming_hackathons_heading_area)
        self.Upcoming_hackathons.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(20)
        font.setBold(True)
        self.Upcoming_hackathons.setFont(font)
        self.Upcoming_hackathons.setStyleSheet("color: rgb(129, 12, 168);")
        self.Upcoming_hackathons.setObjectName("Upcoming_hackathons")
        self.horizontalLayout_3.addWidget(self.Upcoming_hackathons)
        self.See_All_1 = QtWidgets.QPushButton(self.Upcoming_hackathons_heading_area, clicked= lambda: self.HackCall(self.email,self.password))
        self.See_All_1.clicked.connect(MainWindow.close)
        self.See_All_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_All_1.setStyleSheet("QPushButton{\n"
"color: rgb(129, 12, 168);\n"
"border:None;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.See_All_1.setFlat(True)
        self.See_All_1.setObjectName("See_All_1")
        self.horizontalLayout_3.addWidget(self.See_All_1, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.Upcoming_hackathons_heading_area)
        self.Hackathons_holder_area = QtWidgets.QFrame(self.Hackathons_and_Internship_area)
        self.Hackathons_holder_area.setStyleSheet("background-color: rgb(45, 3, 59);\n"
"border-radius:40px;")
        self.Hackathons_holder_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Hackathons_holder_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Hackathons_holder_area.setObjectName("Hackathons_holder_area")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.Hackathons_holder_area)
        self.horizontalLayout_17.setContentsMargins(15, 9, 15, -1)
        self.horizontalLayout_17.setSpacing(15)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        mycursor.execute("SELECT COUNT(hack_id) FROM hackathons_data2;")
        self.count_hacks = mycursor.fetchone()
        self.count_hacks = int(self.count_hacks[0])
        mycursor.execute("SELECT name FROM hackathons_data2 WHERE hack_id = %s;"%self.count_hacks)
        self.name_of_hack1 = mycursor.fetchone()
        self.count_hacks = self.count_hacks - 1
        self.Hack_1_pb = QtWidgets.QPushButton(self.Hackathons_holder_area, clicked = lambda: self.HackCall(self.email,self.password))
        self.Hack_1_pb.clicked.connect(MainWindow.close)
        self.Hack_1_pb.setText(self.name_of_hack1[0])
        self.Hack_1_pb.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(26)
        font.setBold(True)
        self.Hack_1_pb.setFont(font)
        self.Hack_1_pb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Hack_1_pb.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:50px;\n"
"    background-image: url(:/images/media/image1.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/images/media/image11.png);\n"
"}")
        self.Hack_1_pb.setObjectName("Hack_1_pb")
        self.horizontalLayout_17.addWidget(self.Hack_1_pb)
        mycursor.execute("SELECT name FROM hackathons_data2 WHERE hack_id = %s;"%self.count_hacks)
        self.name_of_hack2 = mycursor.fetchone()
        self.count_hacks = self.count_hacks - 1
        self.Hack_2_pb = QtWidgets.QPushButton(self.Hackathons_holder_area, clicked = lambda: self.HackCall(self.email,self.password))
        self.Hack_2_pb.clicked.connect(MainWindow.close)
        self.Hack_2_pb.setText(self.name_of_hack2[0])
        self.Hack_2_pb.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(26)
        font.setBold(True)
        self.Hack_2_pb.setFont(font)
        self.Hack_2_pb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Hack_2_pb.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-image: url(:/images/media/image2.png);\n"
"border-radius:50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/images/media/image21.png);\n"
"}")
        self.Hack_2_pb.setObjectName("Hack_2_pb")
        self.horizontalLayout_17.addWidget(self.Hack_2_pb)
        mycursor.execute("SELECT name FROM hackathons_data2 WHERE hack_id = %s;"%self.count_hacks)
        self.name_of_hack3 = mycursor.fetchone()
        self.Hack_3_pb = QtWidgets.QPushButton(self.Hackathons_holder_area, clicked = lambda: self.HackCall(self.email,self.password))
        self.Hack_3_pb.clicked.connect(MainWindow.close)
        self.Hack_3_pb.setText(self.name_of_hack3[0])
        self.Hack_3_pb.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(26)
        font.setBold(True)
        self.Hack_3_pb.setFont(font)
        self.Hack_3_pb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Hack_3_pb.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:50px;\n"
"background-image: url(:/images/media/image3.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/images/media/image31.png);\n"
"}")
        self.Hack_3_pb.setObjectName("Hack_3_pb")
        self.horizontalLayout_17.addWidget(self.Hack_3_pb)
        self.verticalLayout_3.addWidget(self.Hackathons_holder_area)
        self.Internship_heading_area = QtWidgets.QFrame(self.Hackathons_and_Internship_area)
        self.Internship_heading_area.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Internship_heading_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Internship_heading_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Internship_heading_area.setObjectName("Internship_heading_area")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Internship_heading_area)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Internships = QtWidgets.QLabel(self.Internship_heading_area)
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(20)
        font.setBold(True)
        self.Internships.setFont(font)
        self.Internships.setStyleSheet("color: rgb(129, 12, 168);")
        self.Internships.setObjectName("Internships")
        self.horizontalLayout_2.addWidget(self.Internships)
        self.See_All_2 = QtWidgets.QPushButton(self.Internship_heading_area, clicked = lambda: self.InternCall(self.email,self.password))
        self.See_All_2.clicked.connect(MainWindow.close)
        self.See_All_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_All_2.setStyleSheet("QPushButton{\n"
"color: rgb(129, 12, 168);\n"
"border:None;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.See_All_2.setFlat(True)
        self.See_All_2.setObjectName("See_All_2")
        self.horizontalLayout_2.addWidget(self.See_All_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addWidget(self.Internship_heading_area)
        self.Internships_holder_area = QtWidgets.QFrame(self.Hackathons_and_Internship_area)
        self.Internships_holder_area.setStyleSheet("background-color: rgb(45, 3, 59);\n"
"border-radius:40px;")
        self.Internships_holder_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Internships_holder_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Internships_holder_area.setObjectName("Internships_holder_area")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.Internships_holder_area)
        self.horizontalLayout_16.setContentsMargins(15, 9, 15, -1)
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.Intern_1_pb = QtWidgets.QPushButton(self.Internships_holder_area, clicked= lambda: self.InternCall(self.email,self.password))
        self.Intern_1_pb.clicked.connect(MainWindow.close)
        self.Intern_1_pb.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(26)
        font.setBold(True)
        mycursor.execute("SELECT COUNT(Internship_id) FROM Internship_data;")
        self.count_internships = mycursor.fetchone()
        self.count_internships = int(self.count_internships[0])
        mycursor.execute("SELECT name FROM Internship_data WHERE Internship_id = %s;"%self.count_internships)
        self.name_of_internship1 = mycursor.fetchone()
        self.count_internships = self.count_internships - 1
        self.Intern_1_pb.setText(self.name_of_internship1[0])
        self.Intern_1_pb.setFont(font)
        self.Intern_1_pb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Intern_1_pb.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:50px;\n"
"background-image: url(:/images/media/image1.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/images/media/image11.png);\n"
"}")
        self.Intern_1_pb.setObjectName("Intern_1_pb")
        self.horizontalLayout_16.addWidget(self.Intern_1_pb)
        self.Intern_2_pb = QtWidgets.QPushButton(self.Internships_holder_area, clicked = lambda: self.InternCall(self.email,self.password))
        self.Intern_2_pb.clicked.connect(MainWindow.close)
        self.Intern_2_pb.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(26)
        font.setBold(True)
        mycursor.execute("SELECT name FROM Internship_data WHERE Internship_id = %s;"%self.count_internships)
        self.name_of_internship2 = mycursor.fetchone()
        self.count_internships = self.count_internships - 1
        self.Intern_2_pb.setText(self.name_of_internship2[0])
        self.Intern_2_pb.setFont(font)
        self.Intern_2_pb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Intern_2_pb.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-image: url(:/images/media/image2.png);\n"
"border-radius:50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/images/media/image21.png);\n"
"}")
        self.Intern_2_pb.setObjectName("Intern_2_pb")
        self.horizontalLayout_16.addWidget(self.Intern_2_pb)
        self.Intern_3_pb = QtWidgets.QPushButton(self.Internships_holder_area, clicked = lambda: self.InternCall(self.email, self.password))
        self.Intern_3_pb.clicked.connect(MainWindow.close)
        self.Intern_3_pb.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(26)
        font.setBold(True)
        mycursor.execute("SELECT name FROM Internship_data WHERE Internship_id = %s;"%self.count_internships)
        self.name_of_internship3 = mycursor.fetchone()
        self.Intern_3_pb.setText(self.name_of_internship3[0])
        self.Intern_3_pb.setFont(font)
        self.Intern_3_pb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Intern_3_pb.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius:50px;\n"
"background-image: url(:/images/media/image3.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/images/media/image31.png);\n"
"}")
        self.Intern_3_pb.setObjectName("Intern_3_pb")
        self.horizontalLayout_16.addWidget(self.Intern_3_pb)
        self.verticalLayout_3.addWidget(self.Internships_holder_area)
        self.verticalLayout_2.addWidget(self.Hackathons_and_Internship_area)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.information_area = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.information_area.setMinimumSize(QtCore.QSize(0, 400))
        self.information_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.information_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.information_area.setObjectName("information_area")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.information_area)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Devhack_info_area = QtWidgets.QFrame(self.information_area)
        self.Devhack_info_area.setStyleSheet("")
        self.Devhack_info_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Devhack_info_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Devhack_info_area.setObjectName("Devhack_info_area")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Devhack_info_area)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Devhack_info_header = QtWidgets.QLabel(self.Devhack_info_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Devhack_info_header.sizePolicy().hasHeightForWidth())
        self.Devhack_info_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        font.setBold(True)
        self.Devhack_info_header.setFont(font)
        self.Devhack_info_header.setStyleSheet("color: rgb(129, 12, 168);")
        self.Devhack_info_header.setObjectName("Devhack_info_header")
        self.verticalLayout_6.addWidget(self.Devhack_info_header)
        self.Devhack_info = QtWidgets.QLabel(self.Devhack_info_area)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.Devhack_info.setFont(font)
        self.Devhack_info.setStyleSheet("color: rgb(129, 12, 168);")
        self.Devhack_info.setObjectName("Devhack_info")
        self.verticalLayout_6.addWidget(self.Devhack_info)
        self.Read_more_container = QtWidgets.QFrame(self.Devhack_info_area)
        self.Read_more_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Read_more_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Read_more_container.setObjectName("Read_more_container")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Read_more_container)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Read_more_button = QtWidgets.QPushButton(self.Read_more_container)
        self.Read_more_button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(16)
        self.Read_more_button.setFont(font)
        self.Read_more_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Read_more_button.setStyleSheet("QPushButton{\n"
"border-radius: 22px;\n"
"width: 177px;\n"
"height: 47px;\n"
"background-color: rgb(129, 12, 168);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(129, 12, 168);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(45, 3, 59);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.Read_more_button.setObjectName("Read_more_button")
        self.horizontalLayout_5.addWidget(self.Read_more_button, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_6.addWidget(self.Read_more_container)
        self.horizontalLayout_4.addWidget(self.Devhack_info_area)
        self.H_I_C_area = QtWidgets.QFrame(self.information_area)
        self.H_I_C_area.setMinimumSize(QtCore.QSize(400, 0))
        self.H_I_C_area.setMaximumSize(QtCore.QSize(500, 16777215))
        self.H_I_C_area.setStyleSheet("")
        self.H_I_C_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.H_I_C_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.H_I_C_area.setObjectName("H_I_C_area")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.H_I_C_area)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.H_area = QtWidgets.QFrame(self.H_I_C_area)
        self.H_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.H_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.H_area.setObjectName("H_area")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.H_area)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.H_button = QtWidgets.QPushButton(self.H_area)
        self.H_button.setMinimumSize(QtCore.QSize(0, 100))
        self.H_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.H_button.setStyleSheet("border-radius:50px;\n"
"image: url(:/icons/media/hack_circle.png);\n"
"")
        self.H_button.setText("")
        self.H_button.setObjectName("H_button")
        self.horizontalLayout_7.addWidget(self.H_button)
        self.frame_18 = QtWidgets.QFrame(self.H_area)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(129, 12, 168);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(129, 12, 168);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.horizontalLayout_7.addWidget(self.frame_18)
        self.verticalLayout_10.addWidget(self.H_area)
        self.I_area = QtWidgets.QFrame(self.H_I_C_area)
        self.I_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I_area.setObjectName("I_area")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.I_area)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.I_button = QtWidgets.QPushButton(self.I_area)
        self.I_button.setMinimumSize(QtCore.QSize(0, 100))
        self.I_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.I_button.setStyleSheet("border-radius:50px;\n"
"image: url(:/icons/media/internship_circle.png);")
        self.I_button.setText("")
        self.I_button.setObjectName("I_button")
        self.horizontalLayout_6.addWidget(self.I_button)
        self.frame_20 = QtWidgets.QFrame(self.I_area)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(129, 12, 168);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(129, 12, 168);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.horizontalLayout_6.addWidget(self.frame_20)
        self.verticalLayout_10.addWidget(self.I_area)
        self.C_area = QtWidgets.QFrame(self.H_I_C_area)
        self.C_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.C_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.C_area.setObjectName("C_area")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.C_area)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.C_button = QtWidgets.QPushButton(self.C_area)
        self.C_button.setMinimumSize(QtCore.QSize(0, 100))
        self.C_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.C_button.setStyleSheet("border-radius:50px;\n"
"image: url(:/icons/media/contest_circle.png);")
        self.C_button.setText("")
        self.C_button.setObjectName("C_button")
        self.horizontalLayout_8.addWidget(self.C_button)
        self.frame_22 = QtWidgets.QFrame(self.C_area)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(129, 12, 168);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(129, 12, 168);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_9.addWidget(self.label_12)
        self.horizontalLayout_8.addWidget(self.frame_22)
        self.verticalLayout_10.addWidget(self.C_area)
        self.horizontalLayout_4.addWidget(self.H_I_C_area)
        self.verticalLayout_5.addWidget(self.information_area)
        self.frame_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 800))
        self.frame_13.setStyleSheet("")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.frame_13)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(129, 12, 168);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_11.addWidget(self.label_13, 0, QtCore.Qt.AlignHCenter)
        self.frame_24 = QtWidgets.QFrame(self.frame_13)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_23 = QtWidgets.QFrame(self.frame_24)
        self.frame_23.setStyleSheet("background-color: rgb(45, 3, 59);\n"
"border-radius: 15px;")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_14 = QtWidgets.QLabel(self.frame_23)
        self.label_14.setMinimumSize(QtCore.QSize(438, 438))
        self.label_14.setStyleSheet("background-image: url(:/images/media/Utkarsh_front.png);\n"
"border-bottom-left-radius:60px;\n"
"border-bottom-right-radius:60px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_12.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.frame_23)
        self.label_15.setMinimumSize(QtCore.QSize(0, 30))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(229, 184, 244);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_12.addWidget(self.label_15, 0, QtCore.Qt.AlignHCenter)
        self.frame_25 = QtWidgets.QFrame(self.frame_23)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Linked_In_U = QtWidgets.QPushButton(self.frame_25, clicked= lambda: self.linkedin_call('Utkarsh'))
        self.Linked_In_U.setMinimumSize(QtCore.QSize(60, 60))
        self.Linked_In_U.setMaximumSize(QtCore.QSize(60, 16777215))
        self.Linked_In_U.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Linked_In_U.setStyleSheet("\n"
"image: url(:/icons/media/LinkedIn-Symbole.png);\n"
"border-radius:30px;")
        self.Linked_In_U.setText("")
        self.Linked_In_U.setObjectName("Linked_In_U")
        self.horizontalLayout_9.addWidget(self.Linked_In_U)
        self.Insta_U = QtWidgets.QPushButton(self.frame_25, clicked= lambda: self.insta_call('Utkarsh'))
        self.Insta_U.setMinimumSize(QtCore.QSize(60, 60))
        self.Insta_U.setMaximumSize(QtCore.QSize(60, 16777215))
        self.Insta_U.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Insta_U.setStyleSheet("image: url(:/icons/media/insta.png);\n"
"border-radius:30px;")
        self.Insta_U.setText("")
        self.Insta_U.setObjectName("Insta_U")
        self.horizontalLayout_9.addWidget(self.Insta_U)
        self.GitHub_U = QtWidgets.QPushButton(self.frame_25, clicked= lambda: self.github_call('Utkarsh'))
        self.GitHub_U.setMinimumSize(QtCore.QSize(60, 60))
        self.GitHub_U.setMaximumSize(QtCore.QSize(60, 16777215))
        self.GitHub_U.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GitHub_U.setStyleSheet("image: url(:/icons/media/github-logo.png);\n"
"border-radius:30px;")
        self.GitHub_U.setText("")
        self.GitHub_U.setObjectName("GitHub_U")
        self.horizontalLayout_9.addWidget(self.GitHub_U)
        self.verticalLayout_12.addWidget(self.frame_25)
        self.horizontalLayout_13.addWidget(self.frame_23)
        self.frame_26 = QtWidgets.QFrame(self.frame_24)
        self.frame_26.setStyleSheet("background-color: rgb(45, 3, 59);\n"
"border-radius: 15px;")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_16 = QtWidgets.QLabel(self.frame_26)
        self.label_16.setMinimumSize(QtCore.QSize(438, 438))
        self.label_16.setStyleSheet("background-image: url(:/images/media/OP_bg.png);\n"
"border-bottom-left-radius:60px;\n"
"border-bottom-right-radius:60px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_13.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.frame_26)
        self.label_17.setMinimumSize(QtCore.QSize(0, 30))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(229, 184, 244);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_13.addWidget(self.label_17, 0, QtCore.Qt.AlignHCenter)
        self.frame_27 = QtWidgets.QFrame(self.frame_26)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Linked_In_O = QtWidgets.QPushButton(self.frame_27, clicked= lambda: self.linkedin_call('Om'))
        self.Linked_In_O.setMinimumSize(QtCore.QSize(60, 60))
        self.Linked_In_O.setMaximumSize(QtCore.QSize(60, 16777215))
        self.Linked_In_O.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Linked_In_O.setStyleSheet("image: url(:/icons/media/LinkedIn-Symbole.png);\n"
"border-radius:30px;")
        self.Linked_In_O.setText("")
        self.Linked_In_O.setObjectName("Linked_In_O")
        self.horizontalLayout_10.addWidget(self.Linked_In_O)
        self.Insta_O = QtWidgets.QPushButton(self.frame_27, clicked= lambda: self.insta_call('Om'))
        self.Insta_O.setMinimumSize(QtCore.QSize(60, 60))
        self.Insta_O.setMaximumSize(QtCore.QSize(60, 16777215))
        self.Insta_O.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Insta_O.setStyleSheet("image: url(:/icons/media/insta.png);\n"
"border-radius:30px;")
        self.Insta_O.setText("")
        self.Insta_O.setObjectName("Insta_O")
        self.horizontalLayout_10.addWidget(self.Insta_O)
        self.GitHub_O = QtWidgets.QPushButton(self.frame_27 ,clicked= lambda: self.github_call('Om'))
        self.GitHub_O.setMinimumSize(QtCore.QSize(60, 60))
        self.GitHub_O.setMaximumSize(QtCore.QSize(60, 16777215))
        self.GitHub_O.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GitHub_O.setStyleSheet("image: url(:/icons/media/github-logo.png);\n"
"border-radius:30px;")
        self.GitHub_O.setText("")
        self.GitHub_O.setObjectName("GitHub_O")
        self.horizontalLayout_10.addWidget(self.GitHub_O)
        self.verticalLayout_13.addWidget(self.frame_27)
        self.horizontalLayout_13.addWidget(self.frame_26)
        self.frame_30 = QtWidgets.QFrame(self.frame_24)
        self.frame_30.setStyleSheet("background-color: rgb(45, 3, 59);\n"
"border-radius: 15px;")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_20 = QtWidgets.QLabel(self.frame_30)
        self.label_20.setMinimumSize(QtCore.QSize(438, 438))
        self.label_20.setStyleSheet("background-image: url(:/images/media/Ambrish.png);\n"
"border-bottom-left-radius:60px;\n"
"border-bottom-right-radius:60px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_15.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.frame_30)
        self.label_21.setMinimumSize(QtCore.QSize(0, 30))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(229, 184, 244);")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_15.addWidget(self.label_21, 0, QtCore.Qt.AlignHCenter)
        self.frame_31 = QtWidgets.QFrame(self.frame_30)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.Linked_In_AM = QtWidgets.QPushButton(self.frame_31, clicked= lambda: self.linkedin_call('Ambrish'))
        self.Linked_In_AM.setMinimumSize(QtCore.QSize(60, 60))
        self.Linked_In_AM.setMaximumSize(QtCore.QSize(60, 16777215))
        self.Linked_In_AM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Linked_In_AM.setStyleSheet("image: url(:/icons/media/LinkedIn-Symbole.png);\n"
"border-radius:30px;")
        self.Linked_In_AM.setText("")
        self.Linked_In_AM.setObjectName("Linked_In_AM")
        self.horizontalLayout_12.addWidget(self.Linked_In_AM)
        self.Insta_AM = QtWidgets.QPushButton(self.frame_31, clicked= lambda: self.insta_call('Ambrish'))
        self.Insta_AM.setMinimumSize(QtCore.QSize(60, 60))
        self.Insta_AM.setMaximumSize(QtCore.QSize(60, 16777215))
        self.Insta_AM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Insta_AM.setStyleSheet("image: url(:/icons/media/insta.png);\n"
"border-radius:30px;")
        self.Insta_AM.setText("")
        self.Insta_AM.setObjectName("Insta_AM")
        self.horizontalLayout_12.addWidget(self.Insta_AM)
        self.GitHub_AM = QtWidgets.QPushButton(self.frame_31, clicked= lambda: self.github_call('Ambrish'))
        self.GitHub_AM.setMinimumSize(QtCore.QSize(60, 60))
        self.GitHub_AM.setMaximumSize(QtCore.QSize(60, 16777215))
        self.GitHub_AM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GitHub_AM.setStyleSheet("image: url(:/icons/media/github-logo.png);\n"
"border-radius:30px;")
        self.GitHub_AM.setText("")
        self.GitHub_AM.setObjectName("GitHub_AM")
        self.horizontalLayout_12.addWidget(self.GitHub_AM)
        self.verticalLayout_15.addWidget(self.frame_31)
        self.horizontalLayout_13.addWidget(self.frame_30)
        self.frame_28 = QtWidgets.QFrame(self.frame_24)
        self.frame_28.setStyleSheet("background-color: rgb(45, 3, 59);\n"
"border-radius: 15px;")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_18 = QtWidgets.QLabel(self.frame_28)
        self.label_18.setMinimumSize(QtCore.QSize(438, 438))
        self.label_18.setStyleSheet("background-image: url(:/images/media/Abhishek.png);\n"
"border-bottom-left-radius:60px;\n"
"border-bottom-right-radius:60px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_14.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.frame_28)
        self.label_19.setMinimumSize(QtCore.QSize(0, 30))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(229, 184, 244);")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_14.addWidget(self.label_19, 0, QtCore.Qt.AlignHCenter)
        self.frame_29 = QtWidgets.QFrame(self.frame_28)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Linked_IN_AB = QtWidgets.QPushButton(self.frame_29, clicked= lambda: self.linkedin_call('Abhishek'))
        self.Linked_IN_AB.setMinimumSize(QtCore.QSize(60, 60))
        self.Linked_IN_AB.setMaximumSize(QtCore.QSize(60, 16777215))
        self.Linked_IN_AB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Linked_IN_AB.setStyleSheet("image: url(:/icons/media/LinkedIn-Symbole.png);\n"
"border-radius:30px;")
        self.Linked_IN_AB.setText("")
        self.Linked_IN_AB.setObjectName("Linked_IN_AB")
        self.horizontalLayout_11.addWidget(self.Linked_IN_AB)
        self.Insta_AB = QtWidgets.QPushButton(self.frame_29, clicked= lambda: self.insta_call('Abhishek'))
        self.Insta_AB.setMinimumSize(QtCore.QSize(60, 60))
        self.Insta_AB.setMaximumSize(QtCore.QSize(60, 16777215))
        self.Insta_AB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Insta_AB.setStyleSheet("image: url(:/icons/media/insta.png);\n"
"border-radius:30px;")
        self.Insta_AB.setText("")
        self.Insta_AB.setObjectName("Insta_AB")
        self.horizontalLayout_11.addWidget(self.Insta_AB)
        self.GitHub_AB = QtWidgets.QPushButton(self.frame_29, clicked= lambda: self.github_call('Abhishek'))
        self.GitHub_AB.setMinimumSize(QtCore.QSize(60, 60))
        self.GitHub_AB.setMaximumSize(QtCore.QSize(60, 16777215))
        self.GitHub_AB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GitHub_AB.setStyleSheet("image: url(:/icons/media/github-logo.png);\n"
"border-radius:30px;")
        self.GitHub_AB.setText("")
        self.GitHub_AB.setObjectName("GitHub_AB")
        self.horizontalLayout_11.addWidget(self.GitHub_AB)
        self.verticalLayout_14.addWidget(self.frame_29)
        self.horizontalLayout_13.addWidget(self.frame_28)
        self.verticalLayout_11.addWidget(self.frame_24)
        self.verticalLayout_5.addWidget(self.frame_13)
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
        self.verticalLayout_5.addWidget(self.frame_15, 0, QtCore.Qt.AlignBottom)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DEVHACK.setText(_translate("MainWindow", "DEVHACK"))
        # self.Hello__User_Name.setText(_translate("MainWindow", "HELLO AMBRISH"))
        self.Home_button.setText(_translate("MainWindow", "HOME"))
        self.Hackathons_button.setText(_translate("MainWindow", "  HACKATHONS  "))
        # self.Organize_button.setText(_translate("MainWindow", "  ORGANIZE  "))
        self.Internships_button.setText(_translate("MainWindow", "  INTERNSHIPS  "))
        self.About_button.setText(_translate("MainWindow", "ABOUT"))
        self.Upcoming_hackathons.setText(_translate("MainWindow", "LATEST HACKATHONS"))
        self.See_All_1.setText(_translate("MainWindow", "See All -->"))
        # self.Hack_1_pb.setText(_translate("MainWindow", "Smart Hackathon"))
        # self.Hack_2_pb.setText(_translate("MainWindow", "Smart Hackathon"))
        # self.Hack_3_pb.setText(_translate("MainWindow", "Smart Hackathon"))
        self.Internships.setText(_translate("MainWindow", "LATEST INTERNSHIPS"))
        self.See_All_2.setText(_translate("MainWindow", "See All -->"))
        # self.Intern_1_pb.setText(_translate("MainWindow", "Internship_1"))
        # self.Intern_2_pb.setText(_translate("MainWindow", "Internship_2"))
        # self.Intern_3_pb.setText(_translate("MainWindow", "Internship_3"))
        self.Devhack_info_header.setText(_translate("MainWindow", "DEVHACK MISSION IS TO INSPIRE DEVELOPERS\n"
"TO BUILD GREAT SOFTWARE."))
        self.Devhack_info.setText(_translate("MainWindow", " Devhack is a platform that provides best portal to gather\n"
" information about the ongoing and upcoming hackathons \n"
"related to various fields and teachnologies. Devhack also \n"
"provides you best portal to organize hackathons. Aparts\n"
" from hackathons, Devhack will also provide information\n"
" about the various internships."))
        self.Read_more_button.setText(_translate("MainWindow", "Read more"))
        self.label_7.setText(_translate("MainWindow", "HACKATHONS"))
        self.label_8.setText(_translate("MainWindow", "Join and create your own\n"
"hackathons"))
        self.label_9.setText(_translate("MainWindow", "INTERNSHIPS"))
        self.label_10.setText(_translate("MainWindow", "Do Internships and build your\n"
"resume"))
        self.label_11.setText(_translate("MainWindow", "CONTESTS"))
        self.label_12.setText(_translate("MainWindow", "Participate in various contests."))
        self.label_13.setText(_translate("MainWindow", "MEET OUR TEAM"))
        self.label_15.setText(_translate("MainWindow", "UTKARSH UTTAM"))
        self.label_17.setText(_translate("MainWindow", "OM PAITHANKAR"))
        self.label_21.setText(_translate("MainWindow", "AMBRISH KUMAR RAI"))
        self.label_19.setText(_translate("MainWindow", "ABHISHEK "))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setWindowTitle("Home Page")
    sys.exit(app.exec_())
