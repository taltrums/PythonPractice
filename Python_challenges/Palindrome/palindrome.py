import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

if __name__ == '__main__':
    print(is_palindrome('hello world'))
    print(is_palindrome("A quick brown fox jumps over a lazy dog"))
    print(is_palindrome('No lemon, no melon'))