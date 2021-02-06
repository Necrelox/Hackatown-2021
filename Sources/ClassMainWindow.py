#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Hackatown-2021
## File description:
## MainWindow
##

import io
import folium
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QtWidgets.QMainWindow):
    def load_ui(self):
        self.window_height = 800
        self.window_width = 1200
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("TODO")
        self.setWindowIcon(QtGui.QIcon('TODO'))

    def load_map(self):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        coordinates = (37.8198, -122.4785)
        m = folium.Map(
            title = "TODO",
            zoom_start = 13,
            location = coordinates
        )
        data = io.BytesIO()
        m.save(data, close_file=False)

        web_view = QWebEngineView()
        web_view.setHtml(data.getvalue().decode())
        widget.setLayout(layout)
        layout.addWidget(web_view)
        self.setCentralWidget(widget)

    def __init__(self):
        super().__init__()
        self.load_ui()
        self.load_map()
