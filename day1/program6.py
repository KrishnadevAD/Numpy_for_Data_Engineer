#concatenation of arrray 
import numpy as np 
x1=np.array([1,2,3])
x2=np.array([4,5,6])
x3=np.array([7,8,9])
joinarray=np.concatenate([x1,x2,x3])
print(joinarray)
#print("888888888888888888888")
# multidimensionall concatenatio 
grip=np.array([[1,2,3],[4,5,6]])
conbined=np.concatenate(grip)
print(conbined)
print("#**********")
conbined1=np.concatenate([grip,grip],axis=1)
print(conbined1)
#print("#8888888")
conbined1=np.vstack([grip,x1])
print(conbined1)
# print("********")
# # conbined1=np.hstack([grip,x1]) # it donot take because there arises the problem
# # print(conbined1)
zy = [[98],[98]]
conbined2 =np.hstack(grip,zy)
print(conbined2)


