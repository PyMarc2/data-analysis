# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuActivity = QtWidgets.QMenu(self.menubar)
        self.menuActivity.setObjectName("menuActivity")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuLogin = QtWidgets.QMenu(self.menubar)
        self.menuLogin.setObjectName("menuLogin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Form = QtWidgets.QAction(MainWindow)
        self.actionLoad_Form.setObjectName("actionLoad_Form")
        self.actionPDF = QtWidgets.QAction(MainWindow)
        self.actionPDF.setObjectName("actionPDF")
        self.actionJPEG = QtWidgets.QAction(MainWindow)
        self.actionJPEG.setObjectName("actionJPEG")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.action_CheckIn = QtWidgets.QAction(MainWindow)
        self.action_CheckIn.setObjectName("action_CheckIn")
        self.action_CheckOut = QtWidgets.QAction(MainWindow)
        self.action_CheckOut.setObjectName("action_CheckOut")
        self.actionCheckIn = QtWidgets.QAction(MainWindow)
        self.actionCheckIn.setObjectName("actionCheckIn")
        self.actionCheckOut = QtWidgets.QAction(MainWindow)
        self.actionCheckOut.setObjectName("actionCheckOut")
        self.actionTransfer = QtWidgets.QAction(MainWindow)
        self.actionTransfer.setObjectName("actionTransfer")
        self.actionPickList = QtWidgets.QAction(MainWindow)
        self.actionPickList.setObjectName("actionPickList")
        self.actionInventory = QtWidgets.QAction(MainWindow)
        self.actionInventory.setObjectName("actionInventory")
        self.actionPickList_2 = QtWidgets.QAction(MainWindow)
        self.actionPickList_2.setObjectName("actionPickList_2")
        self.actionSign_In = QtWidgets.QAction(MainWindow)
        self.actionSign_In.setObjectName("actionSign_In")
        self.actionSign_Out = QtWidgets.QAction(MainWindow)
        self.actionSign_Out.setObjectName("actionSign_Out")
        self.menuActivity.addAction(self.actionInventory)
        self.menuActivity.addAction(self.actionPickList_2)
        self.menuLogin.addAction(self.actionSign_In)
        self.menubar.addAction(self.menuLogin.menuAction())
        self.menubar.addAction(self.menuActivity.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuActivity.setTitle(_translate("MainWindow", "Activity"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuLogin.setTitle(_translate("MainWindow", "Login"))
        self.actionLoad_Form.setText(_translate("MainWindow", "Load Form"))
        self.actionPDF.setText(_translate("MainWindow", "PDF"))
        self.actionJPEG.setText(_translate("MainWindow", "JPEG"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.action_CheckIn.setText(_translate("MainWindow", "Check-In"))
        self.action_CheckOut.setText(_translate("MainWindow", "Check-Out"))
        self.actionCheckIn.setText(_translate("MainWindow", "Check-In"))
        self.actionCheckOut.setText(_translate("MainWindow", "Check-Out"))
        self.actionTransfer.setText(_translate("MainWindow", "Transfer"))
        self.actionPickList.setText(_translate("MainWindow", "Picklist"))
        self.actionInventory.setText(_translate("MainWindow", "Inventory"))
        self.actionPickList_2.setText(_translate("MainWindow", "PickList"))
        self.actionSign_In.setText(_translate("MainWindow", "Sign-In"))
        self.actionSign_Out.setText(_translate("MainWindow", "Sign-Out"))


