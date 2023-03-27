import math_operations
import string_operations
import pytest

# Test math operations
def test_add():
    assert math_operations.add(2, 3) == 5

def test_subtract():
    assert math_operations.subtract(5, 3) == 2

def test_multiply():
    assert math_operations.multiply(2, 3) == 6

def test_divide():
    assert math_operations.divide(6, 3) == 2

    with pytest.raises(ValueError):
        math_operations.divide(6, 0)

def test_power():
    assert math_operations.power(2, 3) == 8

def test_modulus():
    assert math_operations.modulus(7, 3) == 1


# Test string operations
def test_reverse_string():
    assert string_operations.reverse_string("hello world") == "dlrow olleh"

def test_to_uppercase():
    assert string_operations.to_uppercase("hello world") == "HELLO WORLD"

def test_to_lowercase():
    assert string_operations.to_lowercase("HELLO WORLD") == "hello world"

def test_is_palindrome():
    assert string_operations.is_palindrome("racecar") == True
    assert string_operations.is_palindrome("hello") == False

def test_count_vowels():
    assert string_operations.count_vowels("hello world") == 3
    assert string_operations.count_vowels("aeiou") == 5
