import numpy as np 
a=np.arange(1,10).reshape(3,3)
print(a)
print(np.max(a))
print(np.min(a))
print(np.max(a,axis=0))
print(np.max(a,axis=1))

print(np.max(axis=0))
print(np.max(axis=1))
