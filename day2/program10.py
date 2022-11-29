import numpy as np 
b=np.arange(1,10)
print(b)
print(np.min(b))
print(np.max(b))
# creating a raondom array 
rng=np.random.default_rng(seed=101) # seed value is the ( kasko aadhar maa tyo value nikalne )
x=rng.random(10)# seed = 101 , yesai ko aadhar ma random no. nikalne 

print(x)
y=rng.integers(0,10,(10))
print(y)
y=rng.integers(0,10,(3,2))
print(y)
