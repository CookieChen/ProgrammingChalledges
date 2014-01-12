'''
Created on Jan 12, 2014

@author: CookieDog
'''

import unittest
from sorting.RatingTheField import *

class Test(unittest.TestCase):
    cookie = ""
    eve = ""

    def setUp(self):
        self.cookie = Suitor()
        self.eve = Suitor()

    def tearDown(self):
        pass


    def testHeightOfCompareSuitor(self):
        self.cookie.height = 177
        self.eve.height = 158

        self.assertTrue(compareSuitor(self.cookie, self.eve) == 1, "Height Of CompareSuitor()")
        
    def testWeightOfCompareSuitor(self):
        self.cookie.weight = 75
        self.eve.weight = 51
        
        self.assertTrue(compareSuitor(self.eve, self.cookie) == -1, "Weight Of CompareSuitor()")
        
    def testLastNameOfCompareSuitor(self):
        self.cookie.lastName = "Love"
        self.eve.lastName = "Love"
        
        self.assertTrue(compareSuitor(self.cookie, self.eve) == 0, "LastName of CompareSuitor()")
        
    def testFirstNameOfCompareSuitor(self):
        self.cookie.firstName = "Cookie"
        self.eve.firstName = "Cake"
        
        self.assertFalse(compareSuitor(self.cookie, self.eve) == 0, "LastName of CompareSuitor()")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    