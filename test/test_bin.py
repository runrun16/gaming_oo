import unittest

from src.outcome import Outcome
from src.bin import Bin

class TestBin(unittest.TestCase):
    def setUp(self):
        self.outcome_black1 = Outcome("Black", 2)
        self.outcome_black2 = Outcome("Black", 2)
        self.outcome_straight5 = Outcome("Straight 5", 30)

    def test_initilaizer(self):
        bin_empty = Bin()
        self.assertEqual(str(bin_empty), "")

        bin_one_black = Bin(self.outcome_black1)
        self.assertEqual(str(bin_one_black), str(self.outcome_black1)) 

        bin_two_outcomes = Bin(self.outcome_black1, self.outcome_straight5)
        expected_str = str(self.outcome_black1) + "," + str(self.outcome_straight5)
        self.assertEqual(str(bin_two_outcomes), expected_str) 

    def test_add_same_outcome(self):
        bin_to_use = Bin(self.outcome_black1)
        bin_to_use.add(self.outcome_black2)
        self.assertEqual(str(bin_to_use), str(self.outcome_black1))
        bin_to_use.add(self.outcome_straight5)
        expected_str = str(self.outcome_black1) + "," + str(self.outcome_straight5)
        self.assertEqual(str(bin_to_use), expected_str)

    def test_string(self):
        self.assertEqual(str(self.outcome_black1), "Black (odds:2)")

if __name__ == '__main__':
    unittest.main()
