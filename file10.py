import re

def is_valid_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', email))

print("Is 'john@example.com' a valid email?", is_valid_email('john@example.com'))
