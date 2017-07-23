def sum_of_multiples(largest, check):
    multiples = set()
    for i in check:
        for n in range(i, largest, i):
            multiples.add(n)
    return sum(multiples)
