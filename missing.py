import pandas as pd

df =pd.read_csv("C:/Users/Admin/Downloads/dataset - 2020-09-24 (1).csv")

#print(df.head(5))
missing_values= df.isnull().sum()

print(missing_values)

duplicates= df.duplicated().sum()

print(duplicates)

