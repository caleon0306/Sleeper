from sleeper_api.base_api import Base
from sleeper_api.NFL_state import State

DEFAULT_SPORT = "nfl"
DEFAULT_SEASON = State().getCurrentState()["season"]
DEFAULT_WEEK = State().getCurrentState()["week"]

class League(Base):

    #initialize the base API
    def __init__(self, leagueID:str) -> None:

        self.league_base = "https://api.sleeper.app/v1/league/" + leagueID
        self.league_id = leagueID

    #return a dictionary of all league info
    def getAllLeagueInfo(self) -> dict:
        return self._request(self.league_base)
    
    #return all roster information for the league
    def getRosters(self) -> list:
        return self._request(self.league_base + "/rosters")
    
    #return all users in a league
    def getUsers(self) -> list:
        return self._request(self.league_base + "/users")
    
    #returns matchups for the given week, default is current week
    def getMatchupsForWeek(self, week:str = str(DEFAULT_WEEK)) -> list:
        return self._request(self.league_base + "/matchups/" + week)
    
    #TODO GETTING THE PLAYOFF BRACKET
    #TODO SEE IF I CAN FIND LEAGUE ID FROM LAST SEASON

"""
TODO TEST ONCE MATCHUPS ARE OUT
    def getSeasonMatchups(self) -> dict:
        weeklyMatchups = []
        for week in range(1, 19):
"""
    