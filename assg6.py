import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\department_performance.csv")
print(df)
print(df.head())
print(df.tail())
print(df.notnull())
print(df.value_counts().idxmin())