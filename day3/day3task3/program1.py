import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
data = pd.read_csv(r"C:\Users\DELL\Desktop\data science DWIT\day3\day3task3\Seattle2014.csv")
print(data)
PRCP =np.array(data["PRCP"])
print("the Prcp data ",PRCP)
print("the data type is ",PRCP.dtype)
# print(PRCP.describe())
print("the raining day ",np.count_nonzero(PRCP>0))
print("the not raining day ",np.count_nonzero(PRCP<=0))
print("the raining day ",np.count_nonzero(PRCP>10))
print("the raining day ",np.sum((PRCP>0) & (PRCP<5)))
print("the raining day ",np.sum((PRCP>5) & (PRCP<10)))