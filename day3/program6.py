import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
# import seaborn as s
# s.set()
#
data = pd.read_csv('Seattle2014.csv')
rainfall = np.array(data['PRCP'])


# print(rainfall[rainfall > 0])
#
# print("No of days without rain",np.sum(rainfall==0))
# print("No of days with raid",np.sum(rainfall !=0))
# print("No of days with rain more than 10mm",np.sum(rainfall > 10))
# print("No of days with rain more than 5mm ", np.sum((rainfall>5) & (rainfall<10)))
#
# rainy = (rainfall >0)
# print(np.sum(rainy))

#boolean array and masking

x = np.array([[9,4,0,3],
              [8,6,3,1],[3,7,4,0]])
#
# print(x<5)
# #masking
# print(x[x<5])

#seattle 2
rainly = (rainfall>0)
# print(rainly)

days = np.arange(365)
# print(days)
summer = (days > 172) & (days < 262)
print(summer)

#np.median(rainfall[rainfall>0])
print("The Median Precp on Rainy days in :",np.median(rainfall[rainly]))
print("The Median Precp on Summer days in 2014 :",np.median(rainfall[summer]))
print("The Maximum Precp on Summer days in 2014 :",np.max(rainfall[summer]))
print("The Minimum Precp on Non Summer days in 2014 :",np.median(rainfall[rainly & ~summer]))