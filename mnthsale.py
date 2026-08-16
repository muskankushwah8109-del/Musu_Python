import pandas as pd

sales = pd.Series(
    [25000, 30000, 28000, 35000, 32000, 27000],
    index=["January", "February", "March", "April", "May", "June"]
)

print(sales)

print("Total Sales:")
print(sales.sum())

print("Average Sales:")
print(sales.mean())

print("Highest Sales Month:")
print(sales.idxmax())

print("Lowest Sales Month:")
print(sales.idxmin())

print("Sales in Ascending Order:")
print(sales.sort_values())

print("Sorted According to Month Names:")
print(sales.sort_index())