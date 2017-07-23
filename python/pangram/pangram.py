"""Check if a word contains all letters"""


def is_pangram_fast(text):
    """Use magic number alphabet"""
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in text.lower().strip():
            return False
    return True


def is_pangram_concise(text):
    return len({char.lower() for char in text if char.isalpha()}) == 26


is_pangram = is_pangram_fast
