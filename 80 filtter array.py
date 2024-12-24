#NumPy filter array
#if a value at an index is True that element
#is contained in the filtered array
#if the value at the index is false that element is excluded
#from the filtered array

#create an array from the elements on index 0 and 2
import numpy as np
arr=np.array([41,42,43,44])
x=[True,False,True,False]
newarr=arr[x]
print(newarr)