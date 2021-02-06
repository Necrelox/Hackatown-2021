#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Hackatown-2021
## File description:
## AerialMap
##

import folium
import io
from PySide2 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class AerialMap(QWidget):
    def load_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

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
        layout.addWidget(web_view)

    def __init__(self):
        super(AerialMap, self).__init__()
        self.load_ui()
