import requests

import json
import folium


class Position():
    def __init__(self, lat, lon):
        self.__lat = lat
        self.__lon = lon

    @property
    def latitude(self):
        return float(self.__lat)

    @property
    def longitude(self):
        return float(self.__lon)

    def __str__(self):
        return str("Latitude "+str(self.__lat)+" | Longitude "+str(self.__lon))


PEOLE_URL = "http://api.open-notify.org/astros.json"
ISS_POS_URL = "http://api.open-notify.org/iss-now.json"

result = requests.get(PEOLE_URL)
res_coord = requests.get(ISS_POS_URL)
# print(result.status_code)

# print(result.content)
res_coord_json = res_coord.json()
result_json = result.json()
# print(result_json)
list_of_people = []
for people in result_json["people"]:
    list_of_people.append(people["name"])
print(list_of_people)

print(res_coord_json)
position = res_coord_json["iss_position"]
now_coordinates = Position(position["latitude"], position["longitude"])
print(now_coordinates)

myMap = folium.Map(location=[20, 0], tiles="OpenStreetMap", zoom_start=2)

marker = folium.Marker(location=[float(now_coordinates.latitude), float(
    now_coordinates.longitude)], tooltip="ISS")
marker.add_to(myMap)
myMap.save("ISS.html")
