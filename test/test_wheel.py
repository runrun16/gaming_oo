
import unittest
import random

from src.wheel import Wheel
from src.outcome import Outcome
from src.bin import Bin


class testWheel(unittest.TestCase):
    def setUp(self):
        self.wheel = Wheel()
        for i in range(38):
            outcome = Outcome(f"some outcome{i}", i)
            self.wheel.add_outcome(i, outcome)

    def test_add_outcome(self):
        new_outcome = Outcome("new add", 10)
        self.wheel.add_outcome(1, new_outcome)
        self.assertEqual(2, len(self.wheel.get(1)))

    def test_choose(self):
        randomizer = random.Random()
        randomizer.seed(5)
        randomizeds = [randomizer.randint(0, 37) for _ in range(5)]
        self.wheel.random_generator.seed(5)
        for random_num in randomizeds:
            chosen_bin = self.wheel.choose()
            self.assertEqual(
                Bin([Outcome(f"some outcome{random_num}", random_num)]),
                chosen_bin)

