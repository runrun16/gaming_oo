import unittest

from src.outcome import Outcome

class TestOutcome(unittest.TestCase):
    def setUp(self):
        self.outcome_black1 = Outcome("Black", 2)
        self.outcome_black2 = Outcome("Black", 2)
        self.outcome_straight5 = Outcome("Straight 5", 30)

    def test_equality(self):
        self.assertTrue(self.outcome_black1 == self.outcome_black2)
        self.assertFalse(self.outcome_black1 == self.outcome_straight5)

    def test_win_amount(self):
        self.assertEqual(self.outcome_black1.win_amount(10), 10 * 2)
        self.assertEqual(self.outcome_straight5.win_amount(29), 29 * 30)

    def test_string(self):
        self.assertEqual(str(self.outcome_black1), "Black (odds:2)")

    def test_hash(self):
        self.assertEqual(hash(self.outcome_black1), hash(self.outcome_black2))
        self.assertNotEqual(hash(self.outcome_black2), hash(self.outcome_straight5))

if __name__ == '__main__':
    unittest.main()
