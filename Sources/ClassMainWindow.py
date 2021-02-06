#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Hackatown-2021
## File description:
## MainWindow
##

import io
import folium
import requests

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

        getter_api = requests.get("http://api.waqi.info/feed/here/?token=fbd6653ea37a6ad41658f86ea896e3c5f22a31f0")
        locat = getter_api.json()['data']['city']['geo']
        city = getter_api.json()['data']['city']['name']

        m = folium.Map(location=locat, zoom_start=15, no_touch=True)
        city_marker = folium.Marker(location=locat, popup=city)
        m.add_child(city_marker)

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
