

def extract_upper(phrase):
    return list(filter(str.isupper, phrase ))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))


if __name__ == '__main__':
    print('[I] Hello from helpers.')