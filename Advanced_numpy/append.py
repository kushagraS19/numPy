# Insert a value at the end of the array.

import numpy as np

arr = np.array([10,20,30,40,50,60])
arr_new = np.append(arr, [80,70,99])
print(arr_new)

arr2 = np.array([[5,6],[7,8]])
arr3 = np.append(arr2 , [9,0])
print(arr3) # Adds in a flatten or 1d array.