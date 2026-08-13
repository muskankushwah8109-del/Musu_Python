
import numpy as np
# Create NumPy array of marks of 10 students
marks = np.array([78, 85, 92, 67, 74, 88, 95, 81, 69, 90])

# Find highest marks
highest = np.max(marks)

# Find lowest marks
lowest = np.min(marks)

# Find average marks
average = np.mean(marks)

# Find standard deviation
std_dev = np.std(marks)

# Display marks greater than 75
greater_75 = marks[marks > 75]

# Sort marks in ascending order
sorted_marks = np.sort(marks)

# Display results
print("Marks:", marks)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Standard Deviation:", std_dev)
print("Marks greater than 75:", greater_75)
print("Marks in ascending order:", sorted_marks)