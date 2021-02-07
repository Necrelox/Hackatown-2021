# -*- coding: utf-8 -*-
##
## HACKATOWN PROJECT, 2021
## Hackatown-2021
## File description:
## main file
##

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_ringProgress(object):
    def setupUi(self, ringProgress):
        if not ringProgress.objectName():
            ringProgress.setObjectName(u"ringProgress")
        ringProgress.resize(335, 373)
        self.centralwidget = QWidget(ringProgress)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame {\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(0, 170, 255, 255));\n"
"}\n"
"")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame {\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame {\n"
"	border-radius: 135px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.container)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 50, 261, 181))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.layoutWidget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Inter Semi Bold")
        font.setPointSize(14)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"background-color:none;\n"
"color: #FFF;")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle, 1, 0, 1, 1)

        self.labelPercentage = QLabel(self.layoutWidget)
        self.labelPercentage.setObjectName(u"labelPercentage")
        font1 = QFont()
        font1.setFamily(u"Lato Light")
        font1.setPointSize(68)
        font1.setBold(False)
        font1.setWeight(50)
        self.labelPercentage.setFont(font1)
        self.labelPercentage.setStyleSheet(u"background-color:none;\n"
"color: #FFF;")
        self.labelPercentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercentage, 2, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        ringProgress.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ringProgress)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 335, 29))
        ringProgress.setMenuBar(self.menubar)

        self.retranslateUi(ringProgress)

        QMetaObject.connectSlotsByName(ringProgress)
    # setupUi

    def retranslateUi(self, ringProgress):
        ringProgress.setWindowTitle(QCoreApplication.translate("ringProgress", u"GuiQt", None))
        self.labelTitle.setText(QCoreApplication.translate("ringProgress", u"<strong>Bernard</strong>", None))
        self.labelPercentage.setText(QCoreApplication.translate("ringProgress", u"<html><head/><body><p>0<span style=\" font-size:58pt; vertical-align:super;\">%</span></p></body></html>", None))
    # retranslateUi
