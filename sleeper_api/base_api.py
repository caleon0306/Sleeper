import requests
import json
from PIL import Image
from io import BytesIO

class Base():
    def _request(self, url : str, image:bool = False) -> dict:
        
        #check if an image is being requested
        if image:
            #check for OK
            try:
                result = requests.get(url)
                result.raise_for_status()
            except requests.exceptions.HTTPError as e:
                return e
            
            try:
                #open and return image
                image_bytes = BytesIO(result.content)
                image = Image.open(image_bytes)
                return image
            except Exception as e:
                return e
            
        #not an image request
        else:
            #ensure the response is OK
            try:
                result = requests.get(url)
                result.raise_for_status()
            except requests.exceptions.HTTPError as e:
                return e
            return result.json()   
