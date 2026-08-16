import pandas as pd

# Temperature for seven days
temp = pd.Series(
    [32, 35, 31, 36, 34, 30, 33],
    index=["Monday", "Tuesday", "Wednesday", "Thursday",
           "Friday", "Saturday", "Sunday"]
)

# Temperature above 33°C
print("Temperature above 33°C:")
print(temp[temp > 33])

# Average temperature
print("Average Temperature:", temp.mean())

# Add 2°C to every day
temp = temp + 2

# Display final Series
print("Final Temperature:")
print(temp)