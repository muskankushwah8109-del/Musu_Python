import numpy as np
import pandas as pd
marks = np.array([78,85,92,67,88])
s = pd.Series(marks,index=["amit","neha","ravi","pooja","karan"])
print(s)
print(s.neha)
print(s.karan)

