from PyQt5 import QtCore, QtGui, QtWidgets
from Homepage import Ui_HomeWindow
def HomeCall(self,email,password):
    self.window = QtWidgets.QMainWindow()
    self.ui = Ui_HomeWindow()
    self.ui.setupUi(self.window,email,password)
    self.window.show()