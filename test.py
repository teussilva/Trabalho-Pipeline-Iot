import pandas as pd

df = pd.read_csv("data/IOT-temp-clean.csv")
print("Colunas do CSV:", df.columns.tolist())
print(df.head())
