import unittest

from add import addition

class TestAddition(unittest.TestCase):

    def testAddition(self):
        self.assertTrue(addition(5, 6) == 11)


if __name__ == "__main__":
    unittest.main()
