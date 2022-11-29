import numpy as np
x=np.arange(0,16).reshape(4,4)
thresold=5
rng=np.random.default_rng(seed=101)# seeds gives the fixed value , no random any refresh time
myarray=rng.integers(10,size=(3,4))
print(myarray)