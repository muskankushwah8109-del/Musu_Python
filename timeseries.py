import numpy as np
import pandas  as pd
data={
    "Date":["2026-01-01","2026-01-02","2026-01-03",
            "2026-01-04","2026-01-05"],
    "Sales":[500,550,520,600,650]
}
df=pd.DataFrame(data)
print(df)
df["Date"]=pd.to_datetime(df["Date"])
print(df.dtypes)
#set data at index
df.set_index("Date",inplace=True)
print(df)
#selection data using date
print(df.loc["2026-01-03"])
print(df.loc["2026-01-02":"2026-01-04"])
#Extract yera and month
df["Year"]=df.index.year
df["Month"]=df.index.month
df["Date"]=df.index.date
print(df)
#data range
dates=pd.date_range(
    start="2026-01-01",
    end="2026-01-07",
    freq="D"
)
print(dates)