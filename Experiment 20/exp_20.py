import numpy as np
arr = np.array([1, 2, 3, 4, 5])

# Mean
print("Mean:", np.mean(arr))

# Median
print("Median:", np.median(arr))

# Standard deviation

print("Standard Deviation:", np.std(arr))

# Variance
print("Variance:", np.var(arr))

# Correlation coefficient
arr2 = np.array([5, 4, 3, 2, 1])
print("Correlation Coefficient:", np.corrcoef(arr, arr2)[0, 1])
