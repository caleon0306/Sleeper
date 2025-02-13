import requests
import json

class Base():
    def _request(self, url : str) -> dict:
        
        #ensure the response is OK
        try:
            result = requests.get(url)
            result.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e
        return result.json()   
