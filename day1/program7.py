import numpy as np 
x=np.array([1,2,3,4,5,6,7,8,9])
print("x\n",x)
# splitting the array 
x1,x2,x3,x4 = np.split(x,[2,4,5])# n-1 value is given 
print("x1",x1)# it prints the value [1,2]
print("x2",x2)# it prints the value [3,4]
print("x3",x3)# it prints the value [5]
print("x4",x4)# it prints the value remainting [6,7,8,9]