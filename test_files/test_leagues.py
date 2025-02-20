import unittest

from requests.exceptions import HTTPError
from sleeper_api.Leagues import League
import requests

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

    #check to make sure getUsers returns a list of dicts
    def testGetUsers(self):
        leagueID = "1180209400990347264"
        leagueOBJ = League(leagueID)

        users = leagueOBJ.getUsers()

        self.assertIsInstance(users, list)
        for user in users:
            self.assertIsInstance(user, dict)

    def testGetMatchups(self):
        #leagues is a league from an already completed season
        leagueID = "1061743196390203392"
        leagueOBJ = League(leagueID)

        matchups = leagueOBJ.getMatchupsForWeek(1)
        self.assertIsInstance(matchups, list)
        for x in matchups:
            self.assertIsInstance(x, dict)

        #test to make sure the correct error is recived for an invalid url
        self.assertIsInstance(leagueOBJ.getMatchupsForWeek("asd"), requests.exceptions.HTTPError)
        #test invalid week returns an empty list
        self.assertEqual(leagueOBJ.getMatchupsForWeek(25), [])

    def testGetPlayoffWinnersBrackets(self):
        #leagues is a league from an already completed season
        leagueID = "1061743196390203392"
        leagueOBJ = League(leagueID)

        bracket = leagueOBJ.getPlayoffWinnersBracket()

        self.assertIsInstance(bracket, list)
        for x in bracket:
            self.assertIsInstance(x, dict)

if __name__ == '__main__':
    unittest.main()