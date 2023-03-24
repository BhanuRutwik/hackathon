def remove_vowels(s):
    return ''.join(c for c in s if c not in 'aeiouAEIOU')

print("String without vowels:", remove_vowels("hello world"))
print("file8")