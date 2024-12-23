#make changes in the view

#make a view change in  the view original array and display both arrays

import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=31
print(arr)
print(x)

#view changes the original array