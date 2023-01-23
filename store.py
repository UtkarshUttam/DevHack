import os
import sys
from PyQt5 import QtWidgets,uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import mysql.connector as mc
from store import *

def passlen(pass1):
    pass1=str(pass1)
    if len(pass1)>=8:
        x=True
    else:
        x=False
    return str(x)

def mobilelen(mobile):
    mobile=str(mobile)
    if len(mobile)==10:
        x=True
    else:
        x=False
    return str(x)

def mobilereg(mobile):
    mydb = mc.connect(host="localhost", user="root", password="root", database="devhack")
    cur = mydb.cursor()
    query1="SELECT MOBILE FROM USER_REG_DATA WHERE MOBILE={}".format(mobile)
    cur.execute(query1)
    temp=cur.fetchone()
    temp=str(temp)
    cur.close()
    if temp == "None":
        x=True
    else:
        x=False
    return str(x)

def checker(email,checkpass):
    mydb = mc.connect(host="localhost", user="root", password="root", database="devhack")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT password FROM user_reg_data WHERE email='{0}'".format(email))
    fetched_password = (mycursor.fetchone())
    fetched_password=fetched_password[0]
    if fetched_password==checkpass:
        x= True
    else:
        x=False
    return x

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
    
