import numpy as np
import pandas as pd
data={'Rollno':[101,101,102],
     'Name':['moku','piyush','SKG'],
     'Marks':[200,300,100]
      }
df=pd.DataFrame(data)
print(df)
print(df.loc[1])