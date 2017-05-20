import datetime

def add_gigasecond(birthday):
    """Return datetime object and add 1 gigasecond"""
    return birthday + datetime.timedelta(seconds=1000000000)