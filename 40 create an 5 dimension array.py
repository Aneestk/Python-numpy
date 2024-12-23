#create an 5 dimension array

#using ndimin using a vector with values 1,2,3,4
#and verify that last dimension has value 4

import numpy as np
arr=np.array([1,2,3,4],ndmin=5)
print(arr)
print("shape of array :",arr.shape)