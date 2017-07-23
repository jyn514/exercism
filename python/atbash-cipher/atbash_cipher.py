from string import ascii_lowercase
try:
        from string import maketrans
        trans = maketrans(ascii_lowercase, "zyxwvutsrqponmlkjihgfedcba")
except ImportError:     # python3
        trans = str.maketrans(ascii_lowercase, "zyxwvutsrqponmlkjihgfedcba")
        
def encode(text):
    """Return an encyphered message with 5 letters per space"""
    text = [x.lower() for x in text if x.isalnum()]
    for i in range(len(text) // 5):
        text.insert((i + 1) * 5 + i, " ")
    return str.translate("".join(text), trans).strip()


def decode(cypher):
    """Return a decyphered message without spaces"""
    return "".join([x for x in str.translate(cypher, trans) if x.isalnum()])
