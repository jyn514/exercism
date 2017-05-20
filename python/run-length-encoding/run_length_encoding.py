def encode(data):
    """Encode a string into a string of form ([int]str)*n; opposite of decode(compressed)"""
    data = list(data)
    structure = []
    index = 0
    while index < len(data):  # don't use `for` loop so that index is mutable
        count = 1
        while (index < len(data) - 1) and (data[index] == data[index + 1]):  # prevent index error && values are equal
            count += 1
            index += 1
        if count > 1:
            structure.append(str(count))  # used only if necessary
        structure.append(data[index])  # the letter that's been iterated
        index += 1
    return "".join(structure)  # return string, not list


def decode(compressed):
    """Decode a string of form ([int]str)*n; opposite of encode(data)"""
    compressed = list(compressed)
    structure = []
    index = 0
    while index < len(compressed):
        try:
            occurences = int(compressed[index])
            structure.append(compressed[index + 1] * occurences)  # doesn't work if number is more than one digit
            index += 1
        except ValueError:
            structure.append(compressed[index])
        index += 1
    return "".join(structure)

