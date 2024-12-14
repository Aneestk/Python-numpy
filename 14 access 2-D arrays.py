#Access 2-D arrays
#to access elments from 2-D arrays we can use
#comma seprated by integers representing the dimension
#and the index of the element

#think of 2-D arrays like a table with raws and columns
#where the dimension represent the raw and the index represent the column

#Access the element on the first raw,second column

import numpy as np
arr= np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('2nd element on 1st raw : ', arr[0,1])