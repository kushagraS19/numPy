# To merge the elements of two or more than two arrays.

"""
np.concatenate((arr1 , arr2) , axis = 0 or 1 or none)
"""

import numpy as np

arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])

arr3 = np.concatenate((arr1 , arr2))
print(arr3)