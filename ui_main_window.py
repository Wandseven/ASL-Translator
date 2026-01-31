# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ADMIN\Downloads\do ab ub\ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.camera = QtWidgets.QLabel(self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(20, 10, 640, 480))
        self.camera.setFrameShape(QtWidgets.QFrame.Box)
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(10, 510, 900, 60))
        self.result.setFrameShape(QtWidgets.QFrame.Box)
        self.result.setText("")
        self.result.setObjectName("result")
        self.mask = QtWidgets.QLabel(self.centralwidget)
        self.mask.setGeometry(QtCore.QRect(700, 60, 196, 196))
        self.mask.setFrameShape(QtWidgets.QFrame.Box)
        self.mask.setText("")
        self.mask.setObjectName("mask")
        self.Startbtn = QtWidgets.QPushButton(self.centralwidget)
        self.Startbtn.setGeometry(QtCore.QRect(720, 292, 151, 51))
        self.Startbtn.setObjectName("Startbtn")
        self.Probtn = QtWidgets.QPushButton(self.centralwidget)
        self.Probtn.setGeometry(QtCore.QRect(720, 360, 151, 51))
        self.Probtn.setObjectName("Probtn")
#        MainWindow.setCentralWidget(self.centralwidget)
 #       self.menubar = QtWidgets.QMenuBar(MainWindow)
  #      self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 21))
   #     self.menubar.setObjectName("menubar")
    #    MainWindow.setMenuBar(self.menubar)
     #   self.statusbar = QtWidgets.QStatusBar(MainWindow)
      #  self.statusbar.setObjectName("statusbar")
       # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Startbtn.setText(_translate("MainWindow", "Start"))
        self.Probtn.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

