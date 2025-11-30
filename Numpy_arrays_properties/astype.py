# To change the data type of the array.
# It is basically type casting of the array.

import numpy as np

arr = np.array([1.5,6.7,7.8,4.6])
int_arr = arr.astype(int)

print(int_arr)
print(int_arr.dtype)