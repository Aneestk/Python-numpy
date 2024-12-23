#NumPy array reshapping

#reshapping arrays
#it means changing the shape of an array
#the shape of an array means the number of elements in the each dimension

#reshape from 1D to 2D
#convert the following 1D arrays with 12 elements into 2D array
#the outer most dimension will have 4 arrays each with 3 elements

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)