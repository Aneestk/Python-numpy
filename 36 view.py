#view:
#make a view chang the original array and display both arrays

import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=42
print(arr)
print(x)

#the view should be affected by the changes made to the original view