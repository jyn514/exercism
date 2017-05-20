def distance(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError
    count=0
    for index, base in enumerate(strand1):
        if base != strand2[index]:
            count+=1
    return count
