import pandas as pd
df=pd.DataFrame({
    "Sales":[100,200,300,400,500,600,700]
})
print(df)
df["Moving_average"]=df["Sales"].rolling(window=3).mean()
print(df)