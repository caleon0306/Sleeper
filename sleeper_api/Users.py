from sleeper_api.base_api import Base


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

        print(result)