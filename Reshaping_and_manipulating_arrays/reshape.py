# It reshape the dimensions of an array without changing its data.
# 1d -> 2d -> 3d
"""
reshape(rows, columns) --> specify new shape if dimensions match.
"""

# Reshaping does not create copy, it returns a view.
# Changing value in the new shape will affect in the original array.

import numpy as np

arr = np.array([10,20,30,40,50,60])
re_arr = arr.reshape(3,2)
print(re_arr)