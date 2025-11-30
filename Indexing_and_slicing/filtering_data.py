# Filtering data based on condition.
# Also known as Boolean masking.

import numpy as np

arr = np.array([10,20,30,40,50,60])

print(arr[arr > 25]) # This returns all the values greater than 25.