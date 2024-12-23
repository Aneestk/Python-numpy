#check if array owns its data

#copiea own the data
#and view does noy wn the data
#but how can we check this? using base
#base that returns None uf the array returns the data
#otherwise the base atribute refer to the original object

#print the value of the base attribute to
#check if an array owns its data or not

import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.copy()
y=arr.view()

print(x.base)
print(y.base)
