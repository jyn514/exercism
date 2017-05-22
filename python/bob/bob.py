def hey(sentence):
    """Imitates a limited conversation."""
    sentence = sentence.strip()
    if sentence == "":            # says nothing
        return 'Fine. Be that way!'
    elif sentence.isupper():      # shouting
        return 'Whoa, chill out!'
    elif sentence.endswith('?'):  # question
        return 'Sure.'
    return 'Whatever.'
