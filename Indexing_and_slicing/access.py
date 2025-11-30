# How to access a single element in an array.

import numpy as np

"""
Syntax : 

array[index] --> For 1d array
array[row , column] --> For 2d or 3d array
"""

arr = np.array([10,20,30,40,50])
print(arr[0])
print(arr[1])
print(arr[3])
print(arr[-1])