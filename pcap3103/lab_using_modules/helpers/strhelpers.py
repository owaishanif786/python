import random
def reverse(phrase):
    return phrase [::-1]

def str_shuffle(phrase):
    l = list(phrase)
    random.shuffle(l)
    shuffled_str = ''.join(l)
    return shuffled_str