import pandas as pd
df=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\employee_sales_dirty_data.csv")
print(df)
print(df.shape)
print(df['Employee_Name'].isnull())
