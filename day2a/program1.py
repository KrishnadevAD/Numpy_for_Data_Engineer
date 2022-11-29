import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
data =pd.read_csv(r'C:\Users\DELL\Desktop\data science DWIT\day2a\president_heights.csv')
#print(data)
#height = data["height(cm)"]
height = np.array(data["height(cm)"])
print("the height of the presidents in cm ",height)
#print(height.size)
#print(data.head())
median=np.median(height)
print("the median height is ",median)
plt.hist(height)
plt.title("height of presidents")
plt.xlabel("height")
plt.ylabel("number")
plt.show()
plt.pie(height)
plt.show()
