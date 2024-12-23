#converting dattypes on existing arrays

#the astype() function create a copy of the array
#and allows you to specify the data type as a parameter

#change data type float to integer by using i as a parameter value

import numpy as np
arr=np.array([1.1,2.1,3.1])
newarr=arr.astype('i')
print(newarr)
print(newarr.dtype)