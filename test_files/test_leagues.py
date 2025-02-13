import unittest

from requests.exceptions import HTTPError
from sleeper_api.Leagues import League

class testLeagues(unittest.TestCase):

    #test to make sure the league initializes correctly
    def testLeagueInitialization(self):
        leagueID = "1180209400990347264"
        leagueOBJ = League(leagueID)

        self.assertEqual(leagueOBJ.league_id, leagueID)
        self.assertIsInstance(leagueOBJ.getAllLeagueInfo(), dict)
        self.assertEqual(leagueOBJ.getAllLeagueInfo()["league_id"], leagueID)

    #test attempting to get information from an invalid league
    def testInvalidLeague(self):
        leagueId = "-12"
        leagueOBJ = League(leagueId)

        self.assertIsInstance(leagueOBJ.getAllLeagueInfo(), HTTPError)
        self.assertEqual(leagueOBJ.getRosters(), None)
        self.assertEqual(leagueOBJ.getUsers(), [])
        self.assertIsInstance(leagueOBJ.getMatchupsForWeek(), HTTPError)

    #check to make sure roster information is a list containing dicts
    def testGetRosters(self):
        leagueID = "1180209400990347264"
        leagueOBJ = League(leagueID)

        rosters = leagueOBJ.getRosters()

        self.assertIsInstance(rosters, list)
        for roster in rosters:
            self.assertIsInstance(roster, dict)

    #TODO TEST ONCE MATCHUPS ARE PUT OUT
    def testInvalidMatchupWeek(self):

        leagueID = "1180209400990347264"
        leagueOBJ =League(leagueID)

        self.assertEqual(leagueOBJ.getMatchupsForWeek(), [])



if __name__ == '__main__':
    unittest.main()