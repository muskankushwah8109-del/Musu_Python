import numpy as np
import pandas as pd
df=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\batsman_runs_ipl.csv")
print(df)
print(df.info())
print(df.shape)
print(df.columns)
print(df.describe())
top15 = df.nlargest(15, 'batsman_run')
print(top15)
print("Mean:", df['batsman_run'].mean())
print("Median:", df['batsman_run'].median())
print("Minimum:", df['batsman_run'].min())
print("Maximum:", df['batsman_run'].max())
print("Standard Deviation:", df['batsman_run'].std())
def performance(runs):
    if runs >= 2500:
        return "Elite"
    elif runs >= 1500:
        return "Excellent"
    elif runs >= 750:
        return "Good"
    else:
        return "Average"

df['performance_level'] = df['batsman_run'].apply(performance)
print(df)
print(df['performance_level'].value_counts())
average = df['batsman_run'].mean()
result = df[df['batsman_run'] > average]
print(result)
average = df['batsman_run'].mean()
df['difference'] = abs(df['batsman_run'] - average)
result = df.loc[df['difference'].idxmin()]
print(result)
sorted_df = df.sort_values('batsman_run', ascending=False)
total_runs = df['batsman_run'].sum()
target = total_runs * 0.25
sorted_df['cumulative_runs'] = sorted_df['batsman_run'].cumsum()
top25 = sorted_df[sorted_df['cumulative_runs'] <= target]
percentage = (len(top25) / len(df)) * 100
print("Percentage:", percentage)
final_df = df[['batter', 'batsman_run', 'performance_level']]

final_df = final_df.sort_values(
    'batsman_run',
    ascending=False
)
print(final_df)