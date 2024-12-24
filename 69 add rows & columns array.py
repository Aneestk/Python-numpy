#add rows and columns

import numpy as np
arr1= np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])
arr2= np.array([[1], [2], [3]])
arr = np.concatenate([arr1,arr2], axis=1)
print(arr)

