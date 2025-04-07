"""tea party exercise"""

__author__: str = "730811132"


def main_planner(guests: int) -> None:
    """Main function computes tea bags, treats, cost"""

    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """Input number of guests and return cups of tea consumed"""
    return 2 * people


def treats(people: int) -> int:
    """Input number of guests and return 1.5 treats based on tea consumed"""
    return int(1.5 * (tea_bags(people=people)))


def cost(tea_count: int, treat_count: int) -> float:
    """Compute the total cost by inputting tea and treat counts"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
