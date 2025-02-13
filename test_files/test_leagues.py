import unittest

from requests.exceptions import HTTPError
from sleeper_api.Leagues import League

class testLeagues(unittest.TestCase):

    #test to make sure the league initializes correctly
    def testLeagueInitialization(self):
        leagueID = "1180209400990347264"
        leagueOBJ = League(leagueID)

        self.assertEqual(leagueOBJ.league_id, leagueID)
        self.assertEqual(leagueOBJ.getAllLeagueInfo()["league_id"], leagueID)

    #test attempting to get information from an invalid league
    def testInvalidLeague(self):
        leagueId = "-12"
        leagueOBJ = League(leagueId)

        self.assertIsInstance(leagueOBJ.getAllLeagueInfo(), HTTPError)
        self.assertEqual(leagueOBJ.getRosters(), None)
        self.assertEqual(leagueOBJ.getUsers(), [])
        self.assertIsInstance(leagueOBJ.getMatchupsForWeek(), HTTPError)

if __name__ == '__main__':
    unittest.main()