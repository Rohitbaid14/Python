import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise operations
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

# Dot product
print("Dot product:", np.dot(arr1, arr2))

# Cross product
print("Cross product:", np.cross(arr1, arr2))