from sleeper_api.base_api import Base

class User(Base):

    def __init__(self, userInput):
        """
        Take a username or user id and get the sleeper user information
        """


        sleeperAPI = "https://api.sleeper.app/v1/user/" + userInput
        result = self._request(sleeperAPI)
        
        if result == None:
            raise TypeError("User not found:", userInput)
            

        self.username = result['username']
        self.id = result['user_id']
        print(self.username)
        print(self.id)
