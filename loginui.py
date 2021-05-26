# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(200, 135)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QSize(200, 135))
        LoginWindow.setMaximumSize(QSize(200, 135))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        LoginWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"Evil_Eye.svg", QSize(), QIcon.Normal, QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 50, 20))
        self.uidBox = QLineEdit(self.centralwidget)
        self.uidBox.setObjectName(u"uidBox")
        self.uidBox.setGeometry(QRect(60, 18, 131, 25))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 52, 50, 20))
        self.pwdBox = QLineEdit(self.centralwidget)
        self.pwdBox.setObjectName(u"pwdBox")
        self.pwdBox.setGeometry(QRect(60, 50, 131, 25))
        self.pwdBox.setMaxLength(10)
        self.pwdBox.setFrame(True)
        self.pwdBox.setEchoMode(QLineEdit.Password)
        self.loginBtn = QPushButton(self.centralwidget)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(50, 90, 101, 31))
        self.loginBtn.setIcon(icon)
        self.loginBtn.setAutoDefault(True)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"\u5b78\u865f", None))
        self.uidBox.setText("")
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"\u5bc6\u78bc", None))
        self.pwdBox.setInputMask("")
        self.pwdBox.setText("")
        self.loginBtn.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
    # retranslateUi

