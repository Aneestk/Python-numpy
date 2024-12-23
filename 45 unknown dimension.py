#Unknown dimension

#you are allowed to have "unknown" dimension
#meaning that you do not have to specify an exact number
#for one of the dimension in the reshape method
#pass -1 as the value, and NumPy will calculate this number for you

#convert 1D arrays with 8 elements to 3D array with 2x2 elements

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
newarr=arr.reshape(2,2,-1)
print(newarr)
#note:we can't pass -1 as more than one dimension