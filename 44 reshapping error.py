#try convert 1-D array with 8 elements  to a 2-D array with 3 elements in each dimension (will raise an error)


import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
newarr=arr.reshape(3,3)
print(newarr)