def slices(text, n):
    if n == 0 or n > len(text):
        raise ValueError
    l = []
    for x in range(len(text) - n + 1):
        substring = text[x : x + n]
        l.append([int(substring[i]) for i in range(len(substring))])
    return l
    
