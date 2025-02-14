import unittest

from sleeper_api.base_api import Base
from sleeper_api.Users import User
from sleeper_api.Leagues import League

class testUsers(unittest.TestCase):
    """
    Test cases for the User class
    """

    def testFindByUsername(self):
        username = "Csonal"
        userOBJ = User(username)

        self.assertEqual(userOBJ.username, "csonal")
        self.assertEqual(userOBJ.user_id, "1061742576467808256")
        self.assertEqual(userOBJ.display_name, "Csonal")
        self.assertEqual(userOBJ.avatar_id, "d55d1f7075eda01948318de4af616075")

    def testFindByUserID(self):
        userID = "1061742576467808256"
        userOBJ = User(userID)

        self.assertEqual(userOBJ.username, "csonal")
        self.assertEqual(userOBJ.user_id, "1061742576467808256")

    def testInvalidUser(self):
        userInput = "-25"

        with self.assertRaises(TypeError):
            User(userInput)        

if __name__ == "__main__":
    unittest.main()