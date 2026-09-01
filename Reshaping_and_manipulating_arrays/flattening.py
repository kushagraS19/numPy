# Converts multi-dimension array into 1d array.

"""
ravel() --> It return the view, modifications in the original array.
flatten() --> It returns the copy of the array, no modifications in the original array.
"""

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr)

arr_2 = arr.flatten()
arr_2[2] = 56
print(arr_2)