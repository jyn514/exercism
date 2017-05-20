def is_isogram(word):
    word=word.lower().strip()
    for letter in word:
        if letter.isalpha() and word.count(letter) > 1:
            return False
    return True
