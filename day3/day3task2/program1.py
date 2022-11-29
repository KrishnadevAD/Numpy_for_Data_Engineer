import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
data = pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day3\day3task2\NFLDATA.csv')
print(data)
#print(data.head()) # first five rows of the data
#print(data.tail())# last five rows of the data
# price = np.array(data['Price'])
# price1 = np.array(data['Price'])
# print("********\n")
# minimum = np.min(price)fully_guaranteed
print("the discription of the data ",data.describe())
fully_guaranteed =np.array(data["fully_guaranteed"])
print("the fully guaranteed data ",fully_guaranteed)
plt.hist(fully_guaranteed)
plt.title("salary")
plt.xlabel("players")
plt.ylabel("salary")

plt.show()