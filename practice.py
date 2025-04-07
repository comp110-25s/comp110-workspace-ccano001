"""Introducing user input and named constants"""

SECRET: str = "punk"


def guess_secret(word: str, secret: str, idx: int = 0) -> bool:
    if len(word) != len(secret):
        print("Words are different lengths")
        return False
    if idx < len(word):
        if word[idx] != secret[idx]:
            print(f"{word[idx]} isn't the secret word's next letter.")
            return False
        else:
            print(
                f"{word[idx]} is at index {idx} for both words! Checking next letters..."
            )
            return guess_secret(word=word, secret=secret, idx=idx + 1)
    else:
        print("They are the same word!")
        return True


print(guess_secret(word=input("What is your word?"), secret=SECRET))
print(guess_secret(word=input("What is your word?"), secret=SECRET, idx=2))
