import unittest

from sleeper_api import base_api
from sleeper_api import Users
from sleeper_api import Leagues
from sleeper_api import NFL_state

#python -m test_files.scratch

if __name__ == "__main__":
    user = "Csonal"
    leagueID2025 = "1180209400990347264"

    #complete 2024 season league
    leagueID2024 = "1061743196390203392"

    userOBJ = Users.User(user)

    leagueOBJ2024 = Leagues.League(leagueID2024)

    trans = leagueOBJ2024.getTransactions(1)
    for x in trans:
        print(type(x))

    #print(leagueOBJ.getMatchupsForWeek("1"))