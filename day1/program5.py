import numpy as np
# x2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x2.reshape(1,0))
x2=np.array(([1,2,3])) # to convert the row into column 
x3=x2[:,np.newaxis]
#print(x3)