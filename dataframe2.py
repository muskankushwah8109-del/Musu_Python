import numpy as np
import pandas as pd
data={'Rollno':[101,101,102],
     'Name':['moku','piyush','SKG'],
     'Marks':[200,300,100]
      }
df=pd.DataFrame(data,index=['m1','m2','m3'])
print(df)