a = 2
b = 32
c = a + b

import unittest

class TestStringMethods(unittest.TestCase):

    def testValues(self):
        self.assertTrue(c == 34)

unittest.main()
