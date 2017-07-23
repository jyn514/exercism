def square_of_sum(n):
    return (n * (n + 1) / 2) ** 2


def sum_of_squares(n):
    return sum([x ** 2 for x in range(n + 1)])


def difference(n):
    return abs(square_of_sum(n) - sum_of_squares(n))
