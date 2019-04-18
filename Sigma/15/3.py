import requests
import json


req = requests.get('https://swapi.co/api/planets/')
print("HTTP Status Code: " + str(req.status_code))

# list_of_planets = json_response["results"]
for planet in range(1, 40):
    req = json.loads(
        requests.get(
            'https://swapi.co/api/planets/'+str(planet)+"/").content)
    if req["name"] == "Kashyyyk":
        kashyyyk = req
        break
'''
# print(req.headers)

json_response = json.loads(req.content)
list_of_planets = json_response["results"]
for planet in list_of_planets:
    if planet["name"] == "Coruscant":
        kashyyyk = planet
        break
# print(kashyyyk)'''


class Planet():
    def __init__(self, **properties):
        self.__dict__.update(properties)


kashyyyk_class = Planet(**kashyyyk)
for film in kashyyyk_class.films:
    req = requests.get(film)
    film_properties = json.loads(req.content)
    # print(film_properties["title"])
    kashyyyk_class.films[kashyyyk_class.films.index(
        film)] = film_properties["title"]
print(kashyyyk_class.__dict__)
print(kashyyyk_class.films)

# print(json_response["results"])
# print("Pokemon Name: " + json_response['name'])
