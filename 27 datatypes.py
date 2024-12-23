#NumPy datatypes
#by defualt python have these datatypes

#string
#integer
#float
#boolean
#complex

#Data types in NumPy

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type(void)


#get the datatype of an aaray object

import numpy as np
arr=np.array([1,2,3,4])
print(arr.dtype)