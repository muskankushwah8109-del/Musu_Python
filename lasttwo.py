import numpy as np
import pandas as pd
s=pd.Series([10,20,30,40,50,60,70])
print(s.head(5))
print(s.tail())
#last two values
print(s.tail(2))
print(s.count())
print(s.describe())
print(s.unique())
print(s.value_counts())
print(s.sort_values(ascending=False))