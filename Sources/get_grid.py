##
## EPITECH PROJECT, 2021
## Hackatown-2021
## File description:
## get_grid
##

import numpy as np

def get_grid(p1, p3, n):
    total = []
    lat_step = np.linspace(p1[0], p3[0], n + 1)
    lon_step = np.linspace(p1[1], p3[1], n + 1)
    lat_pos = lat_step[1] - lat_step[0]
    lon_pos = lon_step[1] - lon_step[0]

    for lat in lat_step[:-1]:
        for lon in lon_step[:-1]:
            p1 = [lon, lat + lat_pos]
            p2 = [lon + lon_pos, lat + lat_pos]
            p3 = [lon + lon_pos, lat]
            p4 = [lon, lat]
            coords = [p1, p2, p3, p4, p1]
            geo_json = {"type": "FeatureCollection",
                "properties":{
                    "lower_left": p4,
                    "upper_right": p1
                },
                "features":[]
            }
            grid_feature = {
                "type":"Feature",
                "geometry":{
                    "type":"Polygon",
                    "coordinates": [coords]
                }
            }
            geo_json["features"].append(grid_feature)
            total.append(geo_json)
    return total
