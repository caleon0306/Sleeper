import unittest

from sleeper_api import base_api
from sleeper_api import Users
from sleeper_api import Leagues

#python -m test_files.scratch

if __name__ == "__main__":
    user = "csonal"
    leagueID = "1180209400990347264"

    userOBJ = Users.User(user)
    
    league = Leagues.League("-12")
    print(type(league.getAllLeagueInfo()))
    
    