"""dictionary test function exercise"""

__author__: str = "730811132"


from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

# invert function


def test_invert_one() -> None:
    """Tests if functions inverts keys"""
    assert invert({"a": "z", "z": "a"}) == {"z": "a", "a": "z"}


def test_invert_two() -> None:
    """Tests if the given dictionary is the same length"""
    same_length: dict["str", "str"] = {"a": "z", "z": "a"}
    assert len(same_length) == len(invert(same_length))


def test_invert_edge() -> None:
    """Tests when both the key and value are the same"""
    assert invert({"z": "z"}) == {"z": "z"}


def test_invert_edge_two() -> None:
    """Empty dict returns empty dict"""
    assert invert({}) == {}


# count function


def test_count_one() -> None:
    """Tests if function correctly counts the string"""
    assert count(["a", "b", "c", "d"]) == {"a": 1, "b": 1, "c": 1, "d": 1}


def test_count_two() -> None:
    """Tests that count for element is at least one"""
    more_zero: dict["str", "int"] = count(["a"])
    assert more_zero["a"] >= 1


def test_count_edge() -> None:
    """Empty List Returns Empty Dict"""
    assert count([]) == {}


# favorite_color function


def test_favorite_one() -> None:
    """Tests if dict correctly returns a str"""
    assert favorite_color({"a": "black", "b": "white", "c": "black"}) == "black"


def test_favorite_two() -> None:
    """Returns most frequent color, even if its the only one"""
    assert favorite_color({"a": "black", "b": "black", "c": "black"}) == "black"


def test_favorite_edge() -> None:
    """If there is a tie, it returns the first color encountered"""
    assert (
        favorite_color({"a": "black", "b": "white", "c": "black", "d": "white"})
        == "black"
    )


def test_favorite_edge_two() -> None:
    """Empty List Returns Empty String"""
    assert favorite_color({}) == ""


# bin_len function


def test_bin_one() -> None:
    """strings are in set with correct length"""
    assert bin_len(["unc", "duke", "wake"]) == {3: {"unc"}, 4: {"duke", "wake"}}


def test_bin_two() -> None:
    """the returned dict does not duplicate keys"""
    assert len(bin_len(["unc", "duke", "wake"])) == 2


def test_bin_edge() -> None:
    """Empty list returns empty dict"""
    assert bin_len([]) == {}
