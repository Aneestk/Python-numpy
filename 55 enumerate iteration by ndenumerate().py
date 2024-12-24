#Enumerated iteration using ndenumerate()

#Enumeration means mentioning sequence number of something one by one

#Sometimes we require corresponding index of the element while iterating
#the ndenumerate() methode can be used for those usecases

#Enumerate on following 1D arrays  elements

import numpy as np
arr=np.array([1,2,3,4,5])

for idx,x in np.ndenumerate(arr):
    print(idx,x)