# reshaping
import numpy as np
x1=np.arange(1,10)
x2=x1.reshape(3,3) # it shapes the value of x1 into 3*3 matrix
print("the value of x1 is ",x1)
print("the value of x2 is ",x2)
x3=np.arange(12,22)
#x4=x3.reshape(3,3)#cannot reshape array of size 10 into shape (3,3)
x4=x3.reshape(2,5)#here array sixe is 10 so , it can reshape into 2*5=10 , 2 = rows , 5= columns

print("the value of x3 is ",x3)
print("the value of x4 is ",x4)
