import pandas as pd
import numpy as nm

df =pd.read_csv("C:/Users/Admin/Downloads/dataset - 2020-09-24 (1).csv")
data = nm.random.normal(df)
select = df.iloc[0:5,]

import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))

plt.hist(data,bins=45,color='blue',alpha=0.7)
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('NAME AND AGE OF EACH PLAYER')
plt.show()