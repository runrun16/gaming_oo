class Bin:
    """Each bin on the wheel

    Attributes:
        outcomes (fronzenset): a fixed set of outcome that match the bin 
    """
    def __init__(self, * outcomes):
        """
        Args:
            outcomes (Outcome): any sequence of outcome
        """
        self.outcomes = frozenset(outcomes)

    def add(self, outcome):
        """Add one outcome that match this bin

        Args:
            outcome (Outcome): outcome to add to this bin
        """
        self.outcomes |= set([outcome])

    def __str__(self):
        return ",".join(map(str, self.outcomes))
        
