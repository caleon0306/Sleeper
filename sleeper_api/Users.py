from sleeper_api.base_api import Base
from PIL import Image


DEFAULT_SPORT = "nfl"
DEFUALT_SEASON = "2025"

class User(Base):

    def __init__(self, userInput) -> None:
        """
        Take a username or user id and get the sleeper user information
        """


        sleeperAPI = "https://api.sleeper.app/v1/user/" + userInput
        result = self._request(sleeperAPI)
        
        if result == None:
            raise TypeError("User not found:", userInput)
            

        self.username = result['username']
        self.user_id = result['user_id']
        self.display_name = result['display_name']
        self.avatar_id = result['avatar']

    #returns an image of the user avatar that can be displayed using .show()
    def getAvatar(self) -> Image.Image:
        return self._request("https://sleepercdn.com/avatars/" + self.avatar_id, image = True)
    
    def getThumbnail(self) -> Image.Image:
        return self._request("https://sleepercdn.com/avatars/thumbs/" + self.avatar_id, image = True)