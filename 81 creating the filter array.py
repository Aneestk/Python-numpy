#Creating the filter array\
#create a filter array thet will return only values higher than 42

import numpy as np
arr=np.array([41,42,43,44])

#create an empty list
filter_arr=[]

#go through each elements in arr
for element in arr:
    #if thr element is higher than 42,set the value to True,
    #otherwise false:
    if element>42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)