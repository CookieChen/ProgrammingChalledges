'''
Created on Jan 12, 2014

@author: CookieDog
'''

import unittest
from sorting.RatingTheField import *

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testHeightOfCompareSuitor(self):
        cookie = Suitor()
        eve = Suitor()
        
        cookie.height = 177
        eve.height = 158

        self.assertTrue(compareSuitor(cookie, eve) == 1, "Height Of CompareSuitor()")
        
    def testWeightOfCompareSuitor(self):
        cookie = Suitor()
        eve = Suitor()
        
        cookie.weight = 75
        eve.weight = 51
        
        self.assertTrue(compareSuitor(eve, cookie) == -1, "Weight Of CompareSuitor()")
        
    def testLastNameOfCompareSuitor(self):
        cookie = Suitor()
        eve = Suitor()
        
        cookie.lastName = "Love"
        eve.lastName = "Love"
        
        self.assertTrue(compareSuitor(cookie, eve) == 0, "LastName of CompareSuitor()")
        
    def testFirstNameOfCompareSuitor(self):
        cookie = Suitor()
        eve = Suitor()
        
        cookie.firstName = "Cookie"
        eve.firstName = "Cake"
        
        self.assertFalse(compareSuitor(cookie, eve) == 0, "LastName of CompareSuitor()")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    