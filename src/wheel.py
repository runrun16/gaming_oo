import random

from src.bin import Bin


BIN_NUM = 38


class Wheel:
    """Keep a tuple of 38 bins 0-36, 37(00), pick a random Bin

    Attributes:
        bins (tuple):a tuple of 38 bins
        random_generator (random): a class of random
    """
    def __init__(self):
        self.bins = tuple(Bin() for i in range(BIN_NUM))
        self.random_generator = random.Random()

    def add_outcome(self, number, outcome):
        """Add outcome to bin at given number
        TODO: instead of using int number, exposing data structure for bins,
        maybe we should accept an input of a string?

        Args:
            number (int): index for the bin
            outcome (Outcome): outcome to add
        """
        self.bins[number].add(outcome)

    def choose(self):
        """Randomly pick a bin

        Returns:
            bin: picked Bin
        """
        return self.random_generator.choice(self.bins)

    def get(self, bin_num):
        """return the bin indexed at bin_num

        Args:
            bin_num (int): bin number
        Return:
            Bin: bin based on input bin num
        """
        return self.bins[bin_num]