from sleeper_api.base_api import Base

class State(Base):

    def __init__(self):

        #link to the nfl state for sleeper
        sleeperAPI = "https://api.sleeper.app/v1/state/nfl"
        result = self._request(sleeperAPI)

        if type(result) is not dict:
            return TypeError("NFL_State State returned:", type(result), "\nExpected Type dict")
        self.cur_state = result
    
    #return dict containing the current state of the NFL season
    def getCurrentState(self) -> dict:
        return self.cur_state