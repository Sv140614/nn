import requests
import json

r=requests.get("https://geocode-maps.yandex.ru/1.x/?geocode=Самара&apikey=3f355b88-81e9-4bbf-a0a4-eb687fdea256&format=json")
geo=json.loads((r.content))
print(geo["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split(" ")[0])
