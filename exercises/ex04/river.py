"""File to define River class."""

__author__: str = "730811132"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """River class is an ecosystem containing Bears and Fish."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes animals after they reach lifespan."""
        bear_survivor: list[Bear] = []  # will store surviving fish
        fish_survivor: list[Fish] = []  # will store surviving bears
        for fish in self.fish:  # will loop through each fish
            if fish.age <= 3:  # checks fish that have not reach end of lifespan
                fish_survivor.append(fish)  # appends surviving fish to new list
        self.fish = fish_survivor  # reassigns fish list to equal new list
        for bear in self.bears:  # will loop through each bear
            if bear.age <= 5:  # checks bear that have not reached end of lifespan
                bear_survivor.append(bear)  # appends surviving bears to new list
        self.bears = bear_survivor  # reassigns bear list to equal new list
        return None

    def bears_eating(self):
        """Tracks and Removes fish that bear eats."""
        for bearss in self.bears:  # loops through each bear
            if len(self.fish) >= 5:  # if there are at least 5 fish
                self.remove_fish(3)  # remove 3 fish from river ecosystem
                bearss.eat(3)  # add 3 counts of fish to the current bear being looped
        return None

    def check_hunger(self):
        """Tracks Bears that starve to death."""
        surviving_bears: list[Bear] = []  # empty list stores surviving bears
        for bear in self.bears:  # loops through each bear
            if bear.hunger_score >= 0:  # if current looped bear hunger_score is >= 0
                surviving_bears.append(bear)  # append that bear to new list
        self.bears = surviving_bears  # reassign bears list to surviving bears new list
        return None

    def repopulate_fish(self):
        """For each pair of Fish, reproduce four fish."""
        four_off: int = (len(self.fish) // 2) * 4  # Each pair of fish = 4 offspring
        for _ in range(0, four_off):  # loops amount of new offspring we have
            self.fish.append(Fish())  # declare offspring Fish and append to Fish list
        return None

    def repopulate_bears(self):
        """For each pair of bears, reproduce one bear."""
        one_off: int = len(self.bears) // 2  # Each pair of bear = 1 offspring
        for _ in range(0, one_off):  # loops amount of new offspring we have
            self.bears.append(Bear())  # declare offspring Bear and append to Bears list
        return None

    def view_river(self):
        """Prints fish and bear population status on given day."""
        print(f"~~~ Day {self.day}: ~~~")  # print day
        print(f"Fish population: {len(self.fish)}")  # print count of fish
        print(f"Bear population: {len(self.bears)}")  # print count of bears
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate a week of life in the river."""
        for _ in range(0, 7):  # will loop totaling 7 iterations
            self.one_river_day()  # calls one_river_day after each iteration

    def remove_fish(self, amount: int):
        """Removes given amount of fish from the river."""
        new_fish: list[Fish] = []  # empty list of fish NOT removed
        count: int = 0  # variable to track fish we have removed so far
        for fish in self.fish:  # loops through each fish
            if count < amount:  # if we haven't reach the amount we want to remove
                count += 1  # do not append to new list,increments count of fish removed
            else:  # we already removed given amount of fish
                new_fish.append(fish)  # appends the remaining fish to new list
        self.fish = new_fish  # reassigns fish list to equal new fish list
