import random

def random_words():
    wl = open('/usr/share/dict/words')
    wordlist = wl.readlines()
    wl.close()
    l = random.choices(wordlist, k=3)
    return l

def _random_word():
    wl = open('/usr/share/dict/words')
    wordlist = wl.readlines()
    wl.close()
    return random.choice(wordlist)


if __name__ == '__main__':
    random_words()