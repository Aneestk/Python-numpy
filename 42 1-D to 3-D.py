#Reshape from 1-D to 3-D


#convert the following 1D arrays with 12 elements into 3D array
#the outermost dimension will have 2 arrays that contains 3 array,each with 2 elements

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(2,3,2)
print(newarr)