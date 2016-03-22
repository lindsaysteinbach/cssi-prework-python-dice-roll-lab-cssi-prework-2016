import sys
import unittest

from dice_roll import *

class TestDiceRoll(unittest.TestCase):

    def test_dice_roll(self):
        #Checks if number is between 1 and 6
        self.assertTrue(1 <= dice_roll() <= 6)
        #Checks if number is an integer
        self.assertTrue(isinstance(dice_roll(),int))
        #Check if numbers in 100 rolls include 1-6
        rolls = []
        for i in xrange(1,100):
            rolls.append(dice_roll())
        for x in xrange(1,6):
            self.assertIn(x,rolls)
        #Check if numbers in 100 rolls don't include 0 and 7
        self.assertNotIn(7,rolls)
        self.assertNotIn(0,rolls)
        

if __name__ == '__main__':
    unittest.main()
