def encode(data):
    """Encode a string into a string of form ([int]str)*n;
       opposite of decode(compressed)"""
    data = list(data)
    structure = []
    index = 0
    while index < len(data):              # index is mutable
        count = 1
        while (index < len(data) - 1) and (data[index] == data[index + 1]):
            # prevent index error && values are equal
            count += 1
            index += 1
        if count > 1:
            structure.append(str(count))  # don't put '1'
        structure.append(data[index])     # data[index] is letter
        index += 1
    return "".join(structure)             # return encoded string


def decode(compressed):
    """Decode a string of form ([int]str)*n;
       opposite of encode(data)"""
    compressed = list(compressed)
    structure = []
    index = 0
    while index < len(compressed):       # index is mutable
        if compressed[index].isdigit():
            occurences = []              # mutable list allows arbitrary digits
            while compressed[index].isdigit():
                occurences.append(compressed[index])
                index += 1
            structure.append(compressed[index] * int("".join(occurences)))
        else:
            structure.append(compressed[index])
        index += 1
    return "".join(structure)
