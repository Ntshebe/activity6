import pandas as pd

df =pd.read_csv("C:/Users/Admin/Downloads/dataset - 2020-09-24 (1).csv")

select = df.iloc[0:5,]

import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))

plt.hist(select['Name'], select['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('NAME AND AGE OF EACH PLAYER')
plt.show()