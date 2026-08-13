import pandas as pd
import numpy as np
data=np.array([[101,'moku',500],
               [102,'rohit',800],
               [103,'mohit',1000]])
c=['Rollno','Name','Marks']
r=['m1','m2','m3']
df=pd.DataFrame(data,r,c)
print(df)