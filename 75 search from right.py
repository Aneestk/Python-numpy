#search from the right side

#find the indexes where the value 7 should be inserted
#sorting from the right

import numpy as np
arr=np.array([6,7,8,9])

x=np.searchsorted(arr,7, side='right')
print(x)