import numpy as np
x1=np.array([[1,2,3],[4,5,6],[7,8,9]])
x1sub =x1[:2,:2,]#.copy()
print("x1",x1sub)

x1sub[0,0]=99
print("x1",x1)
print("x1 sub ",x1sub)