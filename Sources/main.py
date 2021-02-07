#!/usr/bin/env python3
##
## HACKATOWN PROJECT, 2021
## Hackatown-2021
## File description:
## main file
##

import sys
from PyQt5 import QtWidgets
from .ClassMainWindow import MainWindow
from .ClassSplashLoad import SplashLoad

def main():
    app = QtWidgets.QApplication([])
    window = SplashLoad()
    sys.exit(app.exec_())
