import numpy as np
mylist = np.zeros(10,dtype=int)
mylist1 = np.zeros((10,3),dtype=int)
mylist2 = np.ones(10,dtype=int)
print(mylist)
print(mylist1)
print(mylist2)
print(mylist.dtype)
print(mylist1.size)
print(mylist2.shape)
print(mylist.ndim) # ndim is the no. of dimension we have 
print(mylist1.data)
print(mylist2)

