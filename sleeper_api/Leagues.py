from sleeper_api.base_api import Base

DEFAULT_SPORT = "nfl"
DEFAULT_SEASON = "2025"

class League(Base):

    #initialize the base API
    def __init__(self, leagueID:str) -> None:

        self.league_base = "https://api.sleeper.app/v1/league/" + leagueID
        self.league_id = leagueID

    #return a dictionary of all league info
    def getAllLeagueInfo(self) -> dict:
        return self._request(self.league_base)
    
    #return all roster information for the league
    def getRosters(self) -> dict:
        return self._request(self.league_base + "/rosters")
    
    #return all users in a league
    def getUsers(self) -> dict:
        return self._request(self.league_base + "/users")
    
    #returns matchups for the given week, default is one
    def getMatchupsForWeek(self, week:str = "1") -> dict:
        return self._request(self.league_base + "/matchups/" + week)
    