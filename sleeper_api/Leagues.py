from sleeper_api.base_api import Base

DEFAULT_SPORT = "nfl"
DEFAULT_SEASON = "2025"

class League(Base):

    def __init__(self, leagueID:str) -> None:

        self.league_base = "https://api.sleeper.app/v1/league/" + leagueID

    def getAllLeagueInfo(self) -> dict:
        return self._request(self.league_base)
    
    def getRosters(self) -> dict:
        return self._request(self.league_base + "/rosters")