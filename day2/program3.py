#arithmatic unary 
import numpy as np 
x = np.array([1,2,3,4,5])
y= np.array([6,7,8,9,10])
print(-x)
print(x**2)
print(np.sum(x,2))# usnig function,its the numpy builtin , and it is fast than +,-,*,this which is nurmal 
#print(np.subtract(x,2))
#print(np.multiply(x,2))
#print(np.floor_divide(x,2))
#print(np.divide(x,2))