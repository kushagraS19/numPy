# Broadcasting in numpy is performing mathmatical operations without using loops.
# It is fast and more efficient than loops.
# More easier to use.
# It expands smaller arrays into bigger arrays to match them.

import numpy as np 

"""prices = np.array([100,200,300])
discount = 10 # scalar, single value

final_price = prices - (prices * discount/100)

print(final_price)"""

#___________________________________________________________________________________________

# how numpy handle arrays of different shapes. 

# 1. Matching dimensions -- 
# 2. Expanding single elements
# 3. Incompatible shapes

#_____________________________________________________________________________________________

# Broadcasting by single value

"""arr = np.array([100,200,300])
result = arr * 2 # By single value
print(result)"""

#___________________________________________________________________________________________

# Broadcasting from 1d to 2d array

"""matrix = np.array([[1,2,3],[4,5,6]])
vextor = np.array([10,20,30])

result = matrix + vextor
print(result)"""

#___________________________________________________________________________________________

# Incompatible shapes

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([1,2])

haha = arr1 + arr2
print(haha) # It gives a valueError .. because arr1 and arr2 have incompatible shapes.