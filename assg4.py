import numpy as pd 
import pandas as pd
df=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\ipl-matches.csv")
print(df)
print(df.isnull())
print(df.describe())
print(df.value_counts())
print(df.sort_values)