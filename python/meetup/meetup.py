"""Find a date given a string with the weekday, week, month, and year"""

import re
import datetime

class date:
    def __init__(self):
        self.regex = ""
        self.match = 0


year, month, week, day, teenth = date(), date(), date(), date(), date()
year.regex = r"\d{4}"               # 4 digit number
month.regex = r"January|February|March|April|May|June|July|August|September|October|November|December"
    # probably a better way to do this
week.regex = r"first|second|third|fourth|last]"
weekday.regex = r"\b[A-Z]\w+day"        # starts with capital and ends with day
teenth.regex = r"\b[A-Z]\w+teenth"  # starts with capital and ends with teenth

# dictionaries
ordinals = { "first" : 1, "second" : 2, "third" : 3, "fourth" : 4, "last" : -1 }
months = { "January" : 1, "February" : 2, "March" : 3, "April" : 4, "May" : 5,
           "June" : 6, "July" : 7, "August" : 8, "September" : 9, "October" : 10,
           "November" : 11, "December" : 12 }
# dictionaries end

"""Remember: datetime.datetime() takes a tuple of form (year, month, day, . . . )"""


def parse(description):
    """Turn a phrase describing a date into a tuple"""
    date_list = []
    for x in (year, month, week, weekday):
        try:
            temp = re.search(x.regex, description).group()
            if x == week and temp is not 0:
                x.match = ordinals[temp]       # turn word into a number
            elif x == month and temp is not 0:
                x.match = months[temp]
            elif x == year:
                x.match = int(temp)
            elif x == teenth:
                x.match = 1   # TODO
        except AttributeError:   # no matches
                pass             # x.match remains 0
        date_list.append(x.match)
    if 
    return tuple(date_list), bool(teenth.match)      # ((year, month, week, weekday), teenth)


def meetup_day(description):
    meetup_date = parse(description)
    print(locals())
    if meetup_date[4] == 0:  # no mention of -teenth
        meetup_time = datetime.datetime(date)
    else: 
        pass  # TODO
