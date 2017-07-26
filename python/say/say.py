values = { 0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
                   8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
                   15: "fifteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
                   70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred", 1000: "thousand",
                   1e6: "million", 1e9: "billion" }

def say(n):
    """Given an integer, return it as a phrase"""
    if 0 > n or abs(n) >= 1e12 or type(n) not in (int, float):    # 1e12 == one trillion
        raise AttributeError(n)
    elif n in values:
        if n >= 100:
            return "one " + values[n]
        return values[n]
    elif n < 100:
        return "".join(say_under_100(n))
    elif n < 1000:
        return " ".join(say_under_1000(n))
    phrase = []
    for seq in split_num(n):    # string
        phrase += say_under_1000(seq)
    return " ".join(phrase)
    
"""    if -1e12 < n < 0:
        phrase.append("negative")
        n = abs(n)"""

def split_num(n):
    n = str(n)
    chunks = [n[-3:]]     # last 3
    for position in range(-3, - len(n), -3):    # split every three numbers
        chunks.insert(0, n[position - 3 : position])
    return chunks

            
def say_under_100(n):   # takes a int
    if n == 14 or n in range(16, 20):
        return [values[int(str(n)[1])] + "teen"]
    elif n in values or n < 20:
        return [values[n]]
    else:
        return [values[int(str(n)[0]) * 10] + "-" + values[int(str(n)[1])]]
        # append first digit and second digit

def say_under_1000(n):  # takes an int or string
    n = int(n)
    if n < 100:
        return say_under_100(n)
    phrase = []
    first = int(str(n)[0])  # first digit
    phrase.append(values[first])
    if values[first] == 1:
        phrase.append("one")
    phrase.append("hundred")
    n -= first * 100
    if n != 0:
        phrase.append("and")
        phrase += say_under_100(n)
    return phrase
