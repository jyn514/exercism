def sieve(n):
    primes = set()
    composites = [1]
    base, temp = 1, 2
    while base < n:
        base += 1       # effective start is 2
        if base in composites:
            continue
        primes.add(base)
        temp = base
        while temp < n:
            temp += base
            composites.append(temp)
    return sorted(primes)
