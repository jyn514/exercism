def rotate(text, number):
    new = []
    for x in text:
        if ord('a') <= ord(x) <= ord('z'):     # lowercase ascii
            x = ord(x) + number
            if x > ord('z'):                       # no longer lowercase
                x -= 26
            new.append(chr(x))
        elif ord('A') <= ord(x) <= ord('Z'):    # uppercase ascii
            x = ord(x) + number
            if x > ord('Z'):                         # no longer uppercase
                x -= 26
            new.append(chr(x))
        else:
            new.append(x)
    return "".join(new)
