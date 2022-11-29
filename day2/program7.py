# accumulative function
import numpy as np 
b=np.arange(1,10)
print(b)
print(np.sum(b))# it adds the all element of b 
print(np.add.reduce(b))#  list ko sabi items lai reduse gardai add garer dinxa hai guys 
print(np.add.accumulate(b)) # accumulated it see the output hai , every step is added 
# multiply 
print(np.multiply(b))
print(np.multiply.reduce(b))
print(np.multiply.accumulate(b))
print(np.multiply.accumulate(b))
