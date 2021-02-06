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

    def get_data(self):
        loc = requests.get("https://ipinfo.io/json")
        city = loc.json()['city']
        loc = loc.json()['loc']
        loc = loc.split(',')

        getter_api = requests.get("http://api.waqi.info/feed/geo:" + loc[0] + ";" + loc[1] + "/?token=fbd6653ea37a6ad41658f86ea896e3c5f22a31f0")
        if getter_api.json()['status'] != "error":
            pol = getter_api.json()['data']['iaqi']
            dico = {}
            for i in range(len(pol)):
                dico[list(pol)[i]] = list(list(pol.values())[i].values())[0]
            m = folium.Map(location=loc, zoom_start=15, no_touch=True)
            city_marker = folium.Marker(location=loc, popup=city)
            m.add_child(city_marker)
        return m
        

    def load_map(self):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        data = io.BytesIO()
        data_map = self.get_data()
        data_map.save(data, close_file=False)
        web_view = QWebEngineView()
        web_view.setHtml(data.getvalue().decode())
        widget.setLayout(layout)
        layout.addWidget(web_view)
        self.setCentralWidget(widget)















































    def __init__(self):
        super().__init__()
        self.load_ui()
        self.load_map()