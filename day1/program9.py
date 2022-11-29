import numpy as np
mygrid =np.arange(16).reshape(4,4)
print(mygrid)
# hsplit
upper,mid,lower = np.hsplit(mygrid,[2,3])
print("upper",upper)
print("mid",mid)
print("lower",lower)