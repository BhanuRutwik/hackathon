# Script 3: Generate random passwords
import random
import string
def passwordGenerator():
    length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))

    print("Random password generated is:", password)
passwordGenerator()
print("file11")