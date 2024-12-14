#higher dimensional arrays

#an array can have any number of dimensions

#when the array is created
#you can define the number of dimensions by using the "ndmin" argument

#create an array with 5 dimensions and verify that it has 5 dimensions

import numpy as np
arr=np.array([1,2,3,4], ndmin=5)

print(arr)
print("number of dimension :",arr.ndim)