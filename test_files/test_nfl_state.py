import unittest

from sleeper_api.NFL_state import State

#TODO think of how to test more cases since it is constantly changing
class testNFLState(unittest.TestCase):
    def testCreatingObject(self):
        curState = State()
        self.assertIsInstance(curState, State)

    def testGetCurrentState(self):
        curState = State()
        #ensure getCurrentState returns a dict
        self.assertIsInstance(curState.getCurrentState(), dict)


if __name__ == '__main__':
    unittest.main()