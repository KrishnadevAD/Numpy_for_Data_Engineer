import numpy as np
myArray = np.array([1,2,3,4,5,4.55],dtype=float) # here dtype = float will convert all the data into float
print("the numpy array without reversed",myArray)
reversed_arr =myArray[::-1] # it will reverse the numpy array 
print("the reversed array",reversed_arr)