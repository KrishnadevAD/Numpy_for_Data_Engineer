#sub array
import numpy as np
x1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("the value of x1",x1)
xsub = x1[:2,:2]#it will give 2*2 sub array 
print("sub array ",xsub)
# change the value of the subarray 
xsub[0,0]=98 #it will change the value of sub array of matrix position [0,0]
print("the x1 ",x1)
print("the sub array ",xsub)