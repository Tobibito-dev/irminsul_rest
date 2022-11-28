import requests
import json

response = requests.get("https://enka.network/u/701027683/__data.json")
print(response.json())
