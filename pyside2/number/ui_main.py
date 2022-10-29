# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1025, 563)
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 430, 101, 41))
        font = QFont()
        font.setFamily(u"Georgia")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setAutoExclusive(False)
        self.input = QLabel(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(60, 110, 280, 280))
        self.input.setFrameShape(QFrame.Box)
        self.input.setFrameShadow(QFrame.Plain)
        self.input.setLineWidth(2)
        self.output = QLabel(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(670, 190, 331, 81))
        font1 = QFont()
        font1.setFamily(u"\u534e\u6587\u4e2d\u5b8b")
        font1.setPointSize(20)
        self.output.setFont(font1)
        self.output.setFrameShape(QFrame.WinPanel)
        self.output.setAlignment(Qt.AlignCenter)
        self.proc = QLabel(self.centralwidget)
        self.proc.setObjectName(u"proc")
        self.proc.setGeometry(QRect(370, 110, 280, 280))
        self.proc.setFrameShape(QFrame.Box)
        self.proc.setFrameShadow(QFrame.Plain)
        self.proc.setLineWidth(2)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 40, 101, 41))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 40, 191, 41))
        self.label_2.setFont(font2)
        self.label_2.setTextFormat(Qt.MarkdownText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(790, 40, 101, 41))
        self.label_3.setFont(font2)
        self.label_3.setTextFormat(Qt.MarkdownText)
        self.label_3.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1025, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"load", None))
        self.input.setText("")
        self.output.setText("")
        self.proc.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"process", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"output", None))
    # retranslateUi

