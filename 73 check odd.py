#find the indexes where the value are odd?

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])

x=np.where(arr%2==1)  #for odd ==-1

print(x)