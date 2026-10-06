import pandas as pd

df = pd.read_csv("housing_data.csv")

print(df.head())
print(df.info())
print(df.describe())