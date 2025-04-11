"""File to define Bear class."""


class Bear:
    """Class for Bears in an ecosystem."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing the attributes of Bear = Zero."""
        self.age = 0  # inital age attribute is 0
        self.hunger_score = 0  # initial hunger_score is 0
        return None

    def one_day(self):
        """Reassigns attributes after a day."""
        self.age += 1  # add 1 to the age attribute
        self.hunger_score -= 1  # subtract 1 from hunger attribute
        return None

    def eat(self, num_fish: int):
        """Increase the hunger_score by num_fish."""
        self.hunger_score += num_fish  # increment hunger_score by num_fish
