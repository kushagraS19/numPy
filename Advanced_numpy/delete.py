# To delete an element at a specific index of an array.

"""
np.delete(arr, index , axis = none)
"""

import numpy as np

arr = np.array([1,2,3,5,76,8,9])
print(arr)

newarr = np.delete(arr , 4 )
print(newarr)

#____________________________________________________________________________________

# In 2d array -> 

arr_2d = np.array([[1,2,3],[4,5,6]])

newarr2 = np.delete(arr_2d , 0 , axis = 0)
print(newarr2)