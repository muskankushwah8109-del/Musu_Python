import pandas as pd
df1=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\batsman_runs_ipl.csv")
df2=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\movies (2).csv")
print(df1.info())
print(df1.describe())
print(df2.info())
print(df2.describe())
print(df2.isnull().sum())
print(df2.isnull().sum())
n = int(len(df1) * 0.10)
print(df1.sort_values('batsman_run', ascending=False).head(n))
df2['primary_genre'] = df2['genres'].fillna('Unknown').str.split('|').str[0]

genre = df2.groupby('primary_genre').agg(
    movie_count=('title_x', 'count'),
    average_rating=('imdb_rating', 'mean')
)

print(
    genre[genre['movie_count'] >= 20]
    .sort_values('average_rating', ascending=False)
    .head(5)
)
rating_median = df2['imdb_rating'].median()
votes_median = df2['imdb_votes'].median()

print(
    df2[
        (df2['imdb_rating'] > rating_median) &
        (df2['imdb_votes'] > votes_median)
    ]
)
df2['lead_actor'] = df2['actors'].fillna('Unknown').str.split('|').str[0]

print(df2[['title_x', 'actors', 'lead_actor']])

actor_count = df2['lead_actor'].value_counts()

print(actor_count[actor_count >= 3])
import numpy as np

rating = (
    (df2['imdb_rating'] - df2['imdb_rating'].min()) /
    (df2['imdb_rating'].max() - df2['imdb_rating'].min())
)

log_votes = np.log1p(df2['imdb_votes'])

votes = (
    (log_votes - log_votes.min()) /
    (log_votes.max() - log_votes.min())
)

df2['performance_score'] = (rating + votes) / 2

print(df2[['title_x', 'performance_score']])
df2['rank'] = df2['performance_score'].rank(
    ascending=False,
    method='min'
)

print(df2[['title_x', 'performance_score', 'rank']])
print(
    df2.sort_values(
        'performance_score',
        ascending=False
    ).head(20)
)
df1['rank'] = df1['batsman_run'].rank(
    ascending=False,
    method='min'
)

print(
    df1.sort_values('rank').head(20)
    [['batter', 'batsman_run', 'rank']]
)
print(df2.isnull().sum())

df2_clean = df2.dropna(
    subset=['imdb_rating', 'imdb_votes']
)

print(df2_clean.isnull().sum())
print("TOP 10 IPL BATSMEN")
print(
    df1.nlargest(10, 'batsman_run')
    [['batter', 'batsman_run']]
)

print("\nTOP 10 MOVIES")
print(
    df2.nlargest(10, 'performance_score')
    [['title_x', 'imdb_rating', 'imdb_votes',
      'performance_score']]
)

print("\nTOP GENRES")
print(df2['primary_genre'].value_counts().head(10))

print("\nRATING DISTRIBUTION")
print(df2['imdb_rating'].describe())