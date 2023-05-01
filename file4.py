import numpy as np

def sum_of_squares(n):
    print('sum of squares')
    return np.sum(np.arange(1, n+1)**2)

print("Sum of squares of first 5 nos:", sum_of_squares(5))
print("file4")