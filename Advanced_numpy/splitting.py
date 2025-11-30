# To make sub arrays of an array.

"""
np.split(array , n) --> Split the array in equal parts.
n = kitne parts me split karna hai

np.hsplit() --> split horizontally

np.vsplit() --> split vertically (Works only for 2d or 3d dimensional arrays)
"""

import numpy as np

arr = np.array([10,20,30,40,50,60])

print(np.split(arr , 2))
print(np.hsplit(arr, 2))

arr2 = np.array([[3,4],[6,7],[8,9]])
print(np.vsplit(arr2 , 3)) # .vsplit cannot do equal divisionS