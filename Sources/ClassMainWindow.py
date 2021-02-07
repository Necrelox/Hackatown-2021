##
## EPITECH PROJECT, 2021
## Hackatown-2021
## File description:
## MainWindow
##

import io
import folium
import requests
import matplotlib as mpl
import matplotlib.pyplot as plt

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from .get_grid import get_grid

class MainWindow(QtWidgets.QMainWindow):
    def load_ui(self):
        self.window_height = 800
        self.window_width = 1200
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle("Bernard")
        self.setWindowIcon(QtGui.QIcon('../assets/icon.png'))  # icon by: dtafalonso, all credits go to them

    def build_grid(self, loc, m):
        p1 = [float(loc[0]) - 0.03, float(loc[1]) - 0.03]
        p2 = [float(loc[0]) + 0.03, float(loc[1]) + 0.03]
        grid = get_grid(p1, p2, 20)

        for i, geo_json in enumerate(grid):
            color = plt.cm.Reds(i / len(grid))
            color = mpl.colors.to_hex(color)

            gj = folium.GeoJson(
                geo_json,
                style_function=lambda feature,
                color=color: {
                    'fillColor': color,
                    'color':"black",
                    'weight': 2,
                    'dashArray': '5, 5',
                    'fillOpacity': 0.40,
                })
            popup = folium.Popup("Test {}".format(i))
            gj.add_child(popup)
            m.add_child(gj)
        m

    # Using ipinfo.io/json for a more accurate geolocalisation.
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
            m = folium.Map(location=loc, zoom_start=15, no_touch=True, scale_bar=True)
            city_marker = folium.Marker(location=loc, popup=city)
            m.add_child(city_marker)
            self.build_grid(loc, m)
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
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.size = self.geometry()
        self.move((screen.width() - self.size.width()) // 2, (screen.height() - self.size.height()) // 2)
        self.load_map()
