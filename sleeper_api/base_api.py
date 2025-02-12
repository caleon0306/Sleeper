import requests
import json

class Base():
    def request(self, url : str):
        result = requests.get(url)
        print(result)