def is_pangram(word):
    word = word.lower().strip()
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in word:
            return False
    return True

def is_pangram_test(text):
    letters = [char for char in text if char.isalpha()]
    return len(set(letters)) == 26

