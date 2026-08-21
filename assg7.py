import numpy as np
import pandas as pd
df1=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\Students-intregation.csv")
df2=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\Marksheet-intregation.csv")
print(df1)
print(df2)
#print(df2)
df=pd.merge(df1,df2,on="Student_ID")
#print(df)
#print(df[df['Python']>85])
#print(df.nlargest(1,'Total'))
#df.sort_values("Total", ascending=True)
#print(df.head())
#df3=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\Students-intregation.csv").head(5)
#df4=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\Students-intregation.csv").tail(5)
#print(df4)
#df5=pd.concat([df3,df4],ignore_index=True)
#print(df5)
df6=pd.concat([
    df1[["Name","Department"]],df2[["Python","Total"]]],axis=1
)
print(df6)
