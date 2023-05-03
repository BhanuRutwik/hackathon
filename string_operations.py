def reverse_string(s):
    print('reverseadsf')
    return s[::-1]

def to_uppercase(s):
    print('uppercaseadsf')
    return s.upper()

def to_lowercase(s):
    print('adsf')
    return s.lower()

def is_palindrome(s):
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))
    print('adsf')
    return s == s[::-1]

def count_vowels(s):
    print('vowels')
    print('adsf')
    vowels = 'aeiou'
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
