import pandas as pd
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                    111, 112, 113, 114, 115],
    'Name': ['Amit', 'Riya', 'Raj', 'Neha', 'Vikas', 'Pooja', 'Ankit',
             'Sneha', 'Rohit', 'Kavita', 'Manish', 'Priya', 'Arjun', 'Nisha', 'Karan'],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'IT', 'HR', 'Sales',
                   'IT', 'Finance', 'HR', 'IT', 'Sales', 'Finance', 'IT', 'Sales'],
    'Age': [25, 28, 32, 45, 26, 29, 31, 27, 52, 30, 24, 33, 41, 29, 38],
    'Salary': [35000, 42000, 48000, 55000, 39000, None, 52000, 45000,
               60000, 41000, 38000, 50000, 250000, 43000, 70000],
    'Experience': [1, 3, 5, 12, 2, 4, 7, 3, 20, 5, 1, 6, 15, 4, 10],
    'Performance_Score': [72, 80, 85, 78, 90, 75, 88, None, 82, 79,
                          95, 86, 40, 83, 91]
}
df=pd.DataFrame(data)
#print(df.shape)
#print("No of Rows=",df.shape[0])
#print("No of Coloums=",df.shape[1])
#print("Missing Values")
#print(df.isnull().sum())
#print("Repalce salary with Median")
#med=df["Salary"].median
#print(df["Salary"].fillna(med))
#mean=df["Performance_Score"].mean
#print(df["Performance_Score"].fillna(mean))
print(df)
Q1=df['Salary'].quantile(.25)
Q3=df['Salary'].quantile(.75)
IOR=Q3-Q1
print("Q1=",Q1)
print("Q3=",Q3)
print("IOR=",IOR)
lower=Q1-1.5*IOR
upper=Q3+1.5*IOR
print("lower=",lower)
print("upper=",upper)
outliers=df[(df['Salary']<lower) | (df['Salary']>upper)]
#print("outliers=",outliers)
med=df['Salary'].median
print("Mediran=",med)
df.loc[12,"Salary"]=med
print(df)
#df.loc[(df['salary']<lower) | (df['Salary']>upper),"Salary"]=med
#print(df)