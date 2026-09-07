import numpy as np
import pandas  as pd
data={
    "Date":["2026-01-01","2026-01-02","2026-01-03",
            "2026-01-04","2026-01-05"],
    "Sales":[500,550,520,600,650]
}
df=pd.DataFrame(data)
print(df)
#using periods
date=pd.date_range("2026-01-01",end="2026-01-05",freq="D")
print(date)
dates=pd.dates_range("2026-01-08")
#print(dates)