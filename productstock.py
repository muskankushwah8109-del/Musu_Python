import pandas as pd

stock = pd.Series([15, 35, 60, 10, 75, 45],
                  index=["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Speaker"])

stock[stock < 20] = 20

print(stock[stock > 50])
print(len(stock))
print(stock)