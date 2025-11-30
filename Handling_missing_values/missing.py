# We use 3 built-in functions to handle missing values.

# np.isnan() --> detects missing values.
# np.nan_to_num() --> To fill or replace the missing value with another number.
# np.isinf() --> To detect infinite values.

import numpy as np 

# isnan()-->

arr =np.array([1,2,np.nan , 4, 5, np.nan])
print(np.isnan(arr))

# We cannot compare the np.nan values. it just detects the missing values.

#__________________________________________________________________________________________________________

# nan_to_num --> 

# np.nan_to_num(array, nan = vo value jisse replace karna hai (default = 0))

arr2 =np.array([1,2,np.nan , 4, 5, np.nan])
clean = np.nan_to_num(arr2)
print(clean)

#____________________________________________________________________________________________________________

# isinf() -->

# Returns a boolean value.
# A value which exeeds the limit of numbers in py is called infinite values.
# For ex -> 100^1000 , 1 / 0

ar6 = np.array([1,2,np.inf,6,8,np.inf])

print(np.isinf(ar6))

# How to replace infinite values --> 

clean2 = np.nan_to_num(ar6 , posinf = 1000 , neginf = -1000)
print(clean2)