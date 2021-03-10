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
        self.assertEqual(str(bin_empty), "Bin()")

        bin_one_black = Bin([self.outcome_black1])
        self.assertEqual(str(bin_one_black), f"Bin({{{repr(self.outcome_black1)}}})")

        bin_two_outcomes = Bin([self.outcome_black1, self.outcome_straight5])
        expected_str = f"Bin({{{repr(self.outcome_straight5)}, {repr(self.outcome_black1)}}})"
        self.assertEqual(expected_str, str(bin_two_outcomes))

