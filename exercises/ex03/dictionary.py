"""dictionary function exercise"""

__author__: str = "730811132"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary"""
    inverted: dict[str, str] = dict()  # stores our inverted keys and values
    for key in dictionary:  # iterate over the keys in the dictionary
        new_value: str = key  # the new value will be the current key
        new_key: str = dictionary[key]  # the new key will be the current value
        if new_key in inverted:
            raise KeyError("Duplicate Value found")
        inverted[new_key] = (
            new_value  # This links our new_key and new_value in the new dict
        )
    return inverted  # returns the new inverted dictionary


def count(list: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list"""
    frequencies: dict[str, int] = dict()  # empty dictionary
    for key in list:  # iterates for each value of the list
        if key in frequencies:  # if value is found in new dict
            frequencies[key] += 1  # add 1 to the value of the key
        else:  # ensures each key is accounted for
            frequencies[key] = 1  # at least once
    return frequencies  # returns new dictionarry


def favorite_color(popular_color: dict[str, str]) -> str:
    """Returns most frequent color value"""
    colors_list: list[str] = list()  # stores list containing only colors
    for key in popular_color:  # iterate over keys in dictionary
        colors_list.append(popular_color[key])  # Append color value to the colors list
    colors_frequency = count(colors_list)  # converts list to a dict containing counts
    color_count: int = 0  # stores color count based on our new dict
    favorite_color: str = ""  # stores the key of the popular color count
    for color in colors_frequency:  # iterate over keys in colors dictionary
        if (
            colors_frequency[color] > color_count
        ):  # if color count value is greater than color_count
            color_count = colors_frequency[color]  # store int as new color_count value
            favorite_color = (
                color  # the key corresponding to the highest color_count value
            )
    return favorite_color  # returns the popular color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    """Length corresponding to set of words"""
    combine_dict: dict[int, set[str]] = dict()  # empty list stores
    for value in strings:  # iterates through each index in the string
        length: int = len(value)  # length of each string value
        if length not in combine_dict:  # ensures length is only counted once
            combine_dict[length] = set()  # Adds a set as the value for the key
        combine_dict[length].add(
            value
        )  # Adds the word corresponding to the length to the set
    return combine_dict  # returns the dictionary
