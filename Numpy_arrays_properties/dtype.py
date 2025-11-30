# This checks the data types of the elements.

import numpy as np

arr = np.array([1,3,4,67.7]) # if there is a single float value in the array, it still take the whole array as float.
print(arr.dtype)