# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gazer.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_GazerWindow(object):
    def setupUi(self, GazerWindow):
        if not GazerWindow.objectName():
            GazerWindow.setObjectName(u"GazerWindow")
        GazerWindow.resize(500, 360)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GazerWindow.sizePolicy().hasHeightForWidth())
        GazerWindow.setSizePolicy(sizePolicy)
        GazerWindow.setMinimumSize(QSize(500, 360))
        GazerWindow.setMaximumSize(QSize(500, 360))
        font = QFont()
        font.setPointSize(14)
        GazerWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"Evil_Eye.svg", QSize(), QIcon.Normal, QIcon.Off)
        GazerWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(GazerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.courseListView = QListView(self.centralwidget)
        self.courseListView.setObjectName(u"courseListView")
        self.courseListView.setGeometry(QRect(20, 40, 201, 271))
        self.courseListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 81, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 10, 81, 20))
        self.videoListView = QListView(self.centralwidget)
        self.videoListView.setObjectName(u"videoListView")
        self.videoListView.setGeometry(QRect(240, 40, 241, 271))
        self.videoListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.videoListView.setSelectionMode(QAbstractItemView.MultiSelection)
        self.courseBtn = QPushButton(self.centralwidget)
        self.courseBtn.setObjectName(u"courseBtn")
        self.courseBtn.setGeometry(QRect(20, 320, 201, 31))
        font1 = QFont()
        font1.setFamilies([u"\u601d\u6e90\u9ed1\u9ad4 Bold"])
        self.courseBtn.setFont(font1)
        self.courseBtn.setIcon(icon)
        self.gazeBtn = QPushButton(self.centralwidget)
        self.gazeBtn.setObjectName(u"gazeBtn")
        self.gazeBtn.setGeometry(QRect(240, 320, 241, 31))
        self.gazeBtn.setFont(font1)
        self.gazeBtn.setIcon(icon)
        GazerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GazerWindow)

        QMetaObject.connectSlotsByName(GazerWindow)
    # setupUi

    def retranslateUi(self, GazerWindow):
        GazerWindow.setWindowTitle(QCoreApplication.translate("GazerWindow", u"TronGazer", None))
        self.label.setText(QCoreApplication.translate("GazerWindow", u"\u8ab2\u7a0b\u6e05\u55ae", None))
        self.label_2.setText(QCoreApplication.translate("GazerWindow", u"\u5f71\u7247\u6e05\u55ae", None))
        self.courseBtn.setText(QCoreApplication.translate("GazerWindow", u"\u67e5\u8a62", None))
        self.gazeBtn.setText(QCoreApplication.translate("GazerWindow", u"\u89c0\u770b", None))
    # retranslateUi

