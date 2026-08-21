import numpy as np 
import pandas as pd
df=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\ecommerce_analysis.csv")
print(df)
print(df.head())
print(df.value_counts().idxmax())
print(df.value_counts().idxmin())