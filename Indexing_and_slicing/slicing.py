# Extracting subset of data.
# It returns a subset or set of values from the array.

"""
Syntax --> 

array[start : stop : step]

start --> Starting index
stop --> Ending index (It is excluded -- If ending index is 6 the value the end index will be 5)
Step --> Kitne se increement karna hai. (Same as range function in py). By deafault 1
"""

import numpy as np

arr = np.array([10,20,30,40,50,60])

print(arr[1:5]) # From index 1 to 4.
print(arr[:4]) # From index 0 to 3.
print(arr[::2]) # It picks every second element.
print(arr[::-1]) # Reverses the array.  