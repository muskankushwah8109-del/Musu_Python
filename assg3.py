import numpy as np
import pandas as pd
df=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\batsman_runs_ipl.csv")
print(df)
print(df.nunique())
print(df.describe())
print(df.isnull().sum())
print(df.info())