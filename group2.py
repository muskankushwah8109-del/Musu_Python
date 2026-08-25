import pandas as pd
import numpy as np
ipl_data = {
    'Team': [
        'Riders', 'Riders', 'Devils', 'Devils',
        'Kings', 'Kings', 'Kings', 'Kings',
        'Riders', 'Royals', 'Royals', 'Riders'
    ],
    'Rank': [1, 2, 2, 3, 4, 1, 1, 2, 4, 1, 2, 3],
    'Year': [
        2014, 2015, 2014, 2015,
        2014, 2015, 2016, 2017,
        2016, 2014, 2015, 2017
    ],
    'Points': [
        876, 789, 263, 673,
        741, 812, 756, 788,
        694, 701, 804, 690
    ]
}
df = pd.DataFrame(ipl_data)
print(df)
grouped = df.groupby('Team')
print(grouped.get_group('Riders'))
print(grouped['Points'].agg[max()])
print(grouped['Points'].agg[np.mean()])
print(grouped['Points'].agg[np.sum()])
print(grouped['Points'].agg[np.min()])
print(grouped['Points'].agg([np.count]))