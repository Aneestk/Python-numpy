#check number of dimensions

#NumPy arrays provides the "ndim" attribute that returns an integer

#that tells us how many dimension the array have

#check how many dimensions that array have

import numpy as np
a=np.array(42)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)