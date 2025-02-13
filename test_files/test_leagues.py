import unittest

from sleeper_api.Leagues import League

class testLeagues(unittest.TestCase):
    def testLeagueInitialization(self):
        leagueID = "1180209400990347264"
        leagueOBJ = League(leagueID)

        self.assertEqual(leagueOBJ.league_id, leagueID)
        self.assertEqual(leagueOBJ.getAllLeagueInfo()["league_id"], leagueID)

if __name__ == '__main__':
    unittest.main()