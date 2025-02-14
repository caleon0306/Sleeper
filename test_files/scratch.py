import unittest

from sleeper_api import base_api
from sleeper_api import Users
from sleeper_api import Leagues
from sleeper_api import NFL_state

#python -m test_files.scratch

if __name__ == "__main__":
    user = "1290Tyler"
    leagueID = "1180209400990347264"

    userOBJ = Users.User(user)
    leagueOBJ = Leagues.League(leagueID)

    print(NFL_state.State().cur_state)
    print(leagueOBJ.getMatchupsForWeek())