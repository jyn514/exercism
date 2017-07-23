def detect_anagrams(text, possible):
    """Return the subset of possible that is an anagram of text"""
    ana = []
    for i in possible:
        if (all(text.lower().count(letter) == i.lower().count(letter) for letter in i) and
             i.lower() not in text.lower() and len(i) == len(text)):
            ana.append(i)
    return ana
