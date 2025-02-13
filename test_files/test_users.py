import unittest

import sleeper_api.base_api as Base_API
import sleeper_api.Users as User_API
import sleeper_api.Leagues as League_API

class testUsers(unittest.TestCase):
    """
    Test cases for the User class
    """

    def testFindByUsername(self):
        username = "Csonal"
        userOBJ = User_API.User(username)

        self.assertEqual(userOBJ.username, "csonal")
        self.assertEqual(userOBJ.user_id, "1061742576467808256")

    def testFindByUserID(self):
        userID = "1061742576467808256"
        userOBJ = User_API.User(userID)

        self.assertEqual(userOBJ.username, "csonal")
        self.assertEqual(userOBJ.user_id, "1061742576467808256")

    def testInvalidUser(self):
        userInput = "-25"

        with self.assertRaises(TypeError):
            User_API.User(userInput)        

    def testGetAllLeagueIDs(self):
        userID = "1061742576467808256"
        userOBJ = User_API.User(userID)
        self.assertEqual(userOBJ.getAllLeagueIDs(), ['1180209400990347264'])

if __name__ == "__main__":
    unittest.main()