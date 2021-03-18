__all__ = ['extract_upper']

def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

def _sum(a,b):
    return a+b

if __name__ == '__main__':
    print ("Hello from helpers")