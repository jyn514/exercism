def is_leap_year(year):
    """Returns if a year is a leap year. Uses Gregorian calendar."""
    return not year % 4 and (year % 100 or not year % 400)
