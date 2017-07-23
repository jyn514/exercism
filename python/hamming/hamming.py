def distance(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError
    count=0
    for base1, base2 in zip(strand1, strand2):
        if base1 != base2:
            count += 1
    return count
