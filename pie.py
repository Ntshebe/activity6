import pandas as pd

df =pd.read_csv("C:/Users/Admin/Downloads/dataset - 2020-09-24 (1).csv")



import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))

names = df['Name']
age = df['Age']

plt.pie(names,labels=age,autopct='%1.1f%%',startangle=140)

plt.title('NAME AND AGE FOR EACH PLAYER')
plt.show()