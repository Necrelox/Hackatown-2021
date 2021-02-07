#
## HACKATOWN PROJECT, 2021
## Hackatown-2021
## File description:
## ClassSplashLoad
##

from PySide2 import (QtCore, QtGui, QtWidgets)
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from .ClassUi_ringProgress import Ui_ringProgress
from .ClassMainWindow import MainWindow

counter = 0
jumper = 10

class SplashLoad(QtWidgets.QMainWindow):

    def progress (self):
        global counter
        global jumper
        value = counter
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""
        newHtml = htmlText.replace("{VALUE}", str(jumper))
        if(value >= jumper):
            self.ui.labelPercentage.setText(newHtml)
            jumper += 1
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        if counter >= 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter += 0.5

    def progressBarValue(self, value):
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """
        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.ui.circularProgress.setStyleSheet(newStylesheet)

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ringProgress()
        self.ui.setupUi(self)


        screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.size = self.geometry()
        self.move((screen.width() - self.size.width()) // 2, (screen.height() - self.size.height()) // 2)

        self.progressBarValue(0)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(15)
        self.show()
