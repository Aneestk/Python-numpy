#Access 3-D arrays

#to access elements from 3-D arrays we can use
#comm seperated integers representing the dimensions
#and the index of the element

#access the third element of then second array of the first array

import numpy as np
arr = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr[0,1,2])