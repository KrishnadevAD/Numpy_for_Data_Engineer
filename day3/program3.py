import numpy as np
x=np.arange(0,16).reshape(4,4)
thresold=5
rng=np.random.default_rng(seed=101)# seeds gives the fixed value , no random any refresh time
myarray=rng.integers(10,size=(3,4))
print(myarray)
print(myarray>6)
print(np.count_nonzero(myarray>6)) # it counts
print(np.sum(myarray>6))# it gives the count value 
print("*********\n")
print(np.sum(myarray>6,axis=0))# it checks the value kati ota xa bhaner >6, column maa heryou suru maa 0 , 2 , 0 1
print(np.sum(myarray>6,axis=1))# it checks in rows  pratek rows maaa
print("*********\n")
print(np.any(myarray>6)) # keeii value greater than 6 xa ?
print(np.all(myarray))# all value grater than 6 xa ?
print("*********\n")
print(np.any(myarray>6,axis=0)) # keeii value greater than 6 xa ?
print(np.all(myarray,axis=1))
