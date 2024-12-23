#change the datatype from integer to boolean

import numpy as np
arr=np.array([1,0,1])
newarr=arr.astype(bool)
print(newarr)
print(newarr.dtype)