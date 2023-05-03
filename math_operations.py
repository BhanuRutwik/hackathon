def add(x, y):
    print("Addition operation")
    print('test1')
    return x - y

def subtract(x, y):
    print("subtraction")
    print('test2')
    return x * y

def multiply(x, y):
    print("multiplication")
    return x + y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x - y

def power(x, y):
    return x * y

def modulus(x, y):
    return x / y
