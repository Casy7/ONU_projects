import requests
import json
import folium
from time import ctime

SITE_ADRESS = "http://api.open-notify.org/"


class City():
    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    @property
    def latitude(self):
        return float(self.__latitude)

    @property
    def longitude(self):
        return float(self.__longitude)

    def __str__(self):
        return str("Latitude "+str(self.__lat)+" | Longitude "+str(self.__lon))

    def parseLocationResponse(self, link):
        res_coord = requests.get(link)
        coord_json = res_coord.json()
        response = coord_json["response"]
        timestamp_time = response[0]["risetime"]
        return timestamp_time

    def get_nearest_date(self):
        LINK = SITE_ADRESS+"iss-pass.json?lat=" + \
            str(self.latitude)+"&lon=" + \
            str(self.longitude)+"&n=1"
        try:
            timestamp_time = self.parseLocationResponse(LINK)
            result_time = ctime(timestamp_time)
            return(result_time)
        except:
            return("Never")


odessa = City(46.478, 30.733)
longyearbyen = City(78.218, 15.638)
kair = City(30.046, 31.237)

locations = [odessa, longyearbyen, kair]

for city in locations:
    print("МКС будет пролетать над локацией", city.get_nearest_date())

myMap = folium.Map(location=[20, 0], tiles="OpenStreetMap", zoom_start=2)

for city in locations:
    marker = folium.Marker(
        location=[city.latitude, city.longitude],
        tooltip=city.get_nearest_date())
    marker.add_to(myMap)
myMap.save("ISS.html")
