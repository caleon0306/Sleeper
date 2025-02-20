from sleeper_api.base_api import Base
from PIL import Image

from sleeper_api.NFL_state import State

DEFAULT_SPORT = "nfl"
DEFAULT_SEASON = State().getCurrentState()["season"]
DEFAULT_WEEK = State().getCurrentState()["week"]

class User(Base):

    def __init__(self, userInput) -> None:
        """
        Take a username or user id and get the sleeper user information
        """


        self.user_base = "https://api.sleeper.app/v1/user/" + userInput
        result = self._request(self.user_base)
        
        if result == None:
            raise TypeError("User not found:", userInput)
            

        self.username = result['username']
        self.user_id = result['user_id']
        self.display_name = result['display_name']
        self.avatar_id = result['avatar']

        self.user_base = "https://api.sleeper.app/v1/user/" + self.user_id

    #returns an Image.Image object of the user avatar that can be displayed using .show()
    def getAvatar(self) -> Image.Image:
        return self._request("https://sleepercdn.com/avatars/" + self.avatar_id, image = True)
    
    #returns an Image.Image object for the user thumbnail that can be displayed using .show()
    def getThumbnail(self) -> Image.Image:
        return self._request("https://sleepercdn.com/avatars/thumbs/" + self.avatar_id, image = True)
    
    #return all of the leagues a user is in a list of dicts
    def getAllLeagues(self, sport:str = DEFAULT_SPORT, season:str = DEFAULT_SEASON) -> list:
        return self._request(self.user_base + "/leagues/" + sport + "/"+ season)
    
    def getAllDrafts(self, sport:str = DEFAULT_SPORT, season:str = DEFAULT_SEASON) -> list:
        return self._request(self.user_base + "/drafts/" + sport + "/" + str(season))