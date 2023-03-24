import numpy as np

def sum_of_squares(n):
    return np.sum(np.arange(1, n+1)**2)

print("Sum of squares of first 5 numbers:", sum_of_squares(5))
