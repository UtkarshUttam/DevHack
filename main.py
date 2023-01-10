import os
import sys
from PyQt5 import QtWidgets,uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFrame, QStackedWidget, QVBoxLayout, QWidget, QFileDialog, QGridLayout

class StartingWindow(QMainWindow):
    def __init__(self):
        super(StartingWindow,self).__init__()
        uic.loadUi("./Starting_Page.ui",self)
        
        self.button1 = self.findChild(QPushButton, "Get_Started_button")
        self.button1.clicked.connect(self.register_call)
    def register_call(self):
        None
        # screen2 = RegisterWindow()
        # widget.addWidget(screen2)
        # widget.setCurrentIndex(widget.currentIndex()+1)


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