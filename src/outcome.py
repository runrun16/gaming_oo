class Outcome:
    """A single outcome that could be bet on

    Attributes:
        name (int): outcome name
        odss (int): odds: 1
    """

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def win_amount(self, amount):
        """how much win if put amount of bet on this outcome

        Args:
            amount (int): amount put on the bet

        Returns:
            int: how many money win

       """

        return amount * self.odds

    def __eq__(self, other):
        """atrribute equality"""
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __str__(self):
        return "{0} (odds:{1})".format(self.name, self.odds)
