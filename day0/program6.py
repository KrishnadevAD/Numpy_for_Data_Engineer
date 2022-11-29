import numpy as np

mylist = np.arange(0,10,2) # where 0 -> start , 10 -> up to no 10 , 2-> interval 
print(mylist)

print("A\n", np.arange(4).reshape(2, 2), "\n")# arange(4) -> up to no. 4 and reshape(2,2)- 1st=row, 2nd =colum
print("A\n", np.arange(4, 10), "\n")# 4 -> start , 10-> end and by default value step -> 1
print("A\n", np.arange(4, 20, 3), "\n") # start =4 , end = 20 and step = 3