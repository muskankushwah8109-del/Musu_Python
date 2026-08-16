import pandas as pd

salary = pd.Series([40000, 45000, 55000, 60000, 48000, 70000],
                   index=["Amit", "Neha", "Ravi", "Pooja", "Karan", "Rahul"])

# Increase salary by 10%
salary = salary * 1.10

print("Updated Salaries:")
print(salary)

print("Highest Salary Employee:")
print(salary.idxmax())

print("Employees with salary greater than 50000:")
print(salary[salary > 50000])