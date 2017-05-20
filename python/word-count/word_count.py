def word_count(phrase):
    import re
    D = {}
    L = re.split("[\W_]", phrase.lower())
    for word in L:
        D[word] = L.count(word)
    if '' in D:
        del D['']
    return D
