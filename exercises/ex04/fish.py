"""File to define Fish class."""


class Fish:
    """Class for Fish in an ecosystem."""

    age: int

    def __init__(self):
        """Initializing attribute age for Fish."""
        self.age = 0  # initial value of age = 0
        return None

    def one_day(self):
        """Reassigns Fish attributes after a day."""
        self.age += 1  # reassigns age attribute to increase by 1
        return None
