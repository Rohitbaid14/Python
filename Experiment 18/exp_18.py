import numpy as np

# 1D array
arr1 = np.array([1, 2, 3])
print(";1D Array:", arr1)

# 2D array
arr2 = np.array([[1, 2], [3, 4]])
print("2D Array:\n", arr2)

# 3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", arr3)

# Reshaping
reshaped_arr = arr2.reshape(1, 4)
print("Reshaped 2D Array:\n", reshaped_arr)

# Slicing

print("Sliced Array:", arr1[1:3])