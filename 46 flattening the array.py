#flattening the arrays

#flattening arrays means converting a multidimensional array into 1D array

#we can use reshape(-1) to do this

#converting the array into 1D array

import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
neaarr=arr.reshape(-1)
print(neaarr)