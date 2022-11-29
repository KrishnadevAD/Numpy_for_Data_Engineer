import numpy as np
myarray =np.arange(1,10)# it is just like range in python
myarray1 =myarray.reshape(3,3)# print the matrix size accordint to range
#myarray2 =myarray.reshape(2,3)# matrix size not math,cannot reshape array of size 9 into shape (2,3)
print(myarray)
print(myarray1)
#print(myarray2) #cannot reshape array of size 9 into shape (2,3)
