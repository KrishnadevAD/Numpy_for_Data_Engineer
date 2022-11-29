import numpy as np 
a=np.arange(1,5).reshape(2,2)
print(a)
print(np.add.reduce(a))
a=np.arange(1,10).reshape(3,3)
print(a)
print(np.add.reduce(a))