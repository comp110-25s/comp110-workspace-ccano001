"""wordle exercise"""

__author__: str = "730811132"


def contains_char(secret_word: str, letter: str) -> bool:
    """Is the letter in the word?"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    idx: int = 0  # start at index 0
    while idx < len(
        secret_word
    ):  # This loop runs until the index matches the length of the word
        if (
            secret_word[idx] == letter
        ):  # will return True if a letter is contained in the word at a index
            return True
        idx = idx + 1  # moves to the next index and towards making the while loop False
    return False  # letter is not contained through the entire word


def emojified(guess_word: str, secret_word: str) -> str:
    """Color Coding letter based on correct placement"""
    assert len(guess_word) == len(secret_word), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"  # assign variables
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0  # we will start from index 0
    result: str = ""  # empty string to store result
    while idx < len(
        guess_word
    ):  # This loop runs until the index matches the length of the word
        if (
            guess_word[idx] == secret_word[idx]
        ):  # If the guess word and the secret word match at the same index
            result = result + GREEN_BOX  # store green box in the result string
        elif contains_char(
            secret_word, guess_word[idx]
        ):  # guess word and secret word share a similar letter
            result = result + YELLOW_BOX  # store yellow box in result string
        else:  # assume they have no similar characters
            result = result + WHITE_BOX  # store white box in the result string

        idx = idx + 1  # move to the next index
    return result  # return the string that contains the result


def input_guess(N: int) -> str:
    """Is this word N characters long"""
    guess: str = input(
        f"Enter a {N} character word:"
    )  # stores the guess the user inputs in a str
    while N != len(guess):  # safe layer that loops until N equals the len of the word
        guess = input(
            f"That wasn't {N} chars! Try again:"
        )  # prompts user to input a new response
    return guess  # returns validated inputted string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    attempt: int = 1  # store the attempt the user is on
    while attempt <= 6:  # Loops until the user reaches max number of attempts
        print(f"=== Turn {attempt}/6 ===")  # displays current attempt
        guess = input_guess(
            len(secret)
        )  # stores user's guess and validates it is the length of the secret word
        print(emojified(guess, secret))  # displays emojified result str
        if guess == secret:  # if guess word is the exact same string as the secret word
            return print(
                f"You won in {attempt}/6 turns!"
            )  # exits the loop and returns victory prompt after user wins
        attempt = attempt + 1  # move to next attempt if words don't match

    return print("X/6 - Sorry, try again tomorrow!")  # max attempts reached, exit game


if __name__ == "__main__":  # Run in python module
    main(secret="codes")
