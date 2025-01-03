#iterating with different step size

#we can use filtering and followed by iteration,

#iterate through every scalar element of the 2-D array skipping 1 element

import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])

for x in np.nditer(arr[:, ::2]):
    print(x)

#this slice operation selects all rows(:)
#and every second column starting from the first column(::2)
#so it selects column 0 and 2 from the both rows