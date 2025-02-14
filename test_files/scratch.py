import unittest

from sleeper_api import base_api
from sleeper_api import Users
from sleeper_api import Leagues
from sleeper_api import NFL_state

#python -m test_files.scratch

if __name__ == "__main__":
    user = "csonal"
    leagueID = "1180209400990347264"

    curState = NFL_state.State()
    print(curState.getCurrentState())
    
    