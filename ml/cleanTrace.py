import string


def clean_trace(trace):
    punctuation_and_whitespaces = string.punctuation + string.whitespace
    translator = str.maketrans(punctuation_and_whitespaces, ' ' * len(punctuation_and_whitespaces))
    trace = trace.translate(translator)
    return [word.lower() for word in trace.split()]
