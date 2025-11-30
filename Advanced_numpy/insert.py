"""
np.insert(array, index, value, axis = none)

array -> original array
axis -> If it sets to none then the value stored in 1d / flatten array.
        If axis = 1, means the value will store row-wise
        If axis = 2, means the value will store column-wise
"""

import numpy as np

arr = np.array([10,20,30,40,60,65])

new_arr = np.insert(arr, 2, 100) # axis = 0 --> Default
print(new_arr)

#________________________________________________________________________________________________________

# Insert in 2d array -->

arr2d = np.array([[1,2],[3,4]])

new_arr2d = np.insert(arr2d , 1 , [5,6], axis= 1)
print(new_arr2d)