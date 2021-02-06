#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Hackatown-2021
## File description:
## MainWindow
##

from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide2.QtGui import QIcon
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    def set_values(self):
        self.window_height = 800
        self.window_width = 1200
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("TODO")
        self.setWindowIcon(QIcon("TODO.png"))

    def load_ui(self):
        loader = QUiLoader()
        path = "../Widget_ui/form.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_values()
        self.load_ui()
