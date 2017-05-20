def hey(sentence):
    """Imitates a conversation."""
    sentence = sentence.strip()
    if sentence == "":   # says nothing
        return 'Fine. Be that way!'
    elif sentence.endswith('?') and not sentence.isupper(): # question but not shouting
        return 'Sure.'
    elif (sentence.endswith('!') and "'" not in sentence) or sentence.isupper(): # exclamation without contractions
        return 'Whoa, chill out!'
    return 'Whatever.'
