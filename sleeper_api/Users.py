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

    def getAllLeagueIDs(self, sport:str = DEFAULT_SPORT , season:str = DEFUALT_SEASON) -> list[str]:
        
        sleeperAPI = "https://api.sleeper.app/v1/user/" + self.user_id + "/leagues/" + sport + "/" + season
        result = self._request(sleeperAPI)

        #init league ids variable
        self.league_ids = []

        #add all current leagues to leagueIDS
        for curLeague in result:
            self.league_ids.append(curLeague["league_id"])
        
        return self.league_ids