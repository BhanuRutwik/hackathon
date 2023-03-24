import numpy as np

# Generate a random numpy array
arr = np.random.randint(0, 10, size=(5, 5))
print(arr)

# Transpose the array
arr_transposed = arr.T
print(arr_transposed)

# Flatten the array
arr_flattened = arr.flatten()
print(arr_flattened)

# Calculate the sum of the array
arr_sum = np.sum(arr)
print(arr_sum)

