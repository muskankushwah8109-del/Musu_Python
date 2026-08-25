import numpy as np 
import pandas as pd
df=pd.read_csv(r"c:\Users\muska\OneDrive\muskan csf pdf\movies (2).csv")
print(df)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.nunique())
print(df.isnull().sum())
print((df.isnull().sum() / len(df)) * 100)
print(df[
    (df['year_of_release'] >= 2015) &
    (df['imdb_rating'] >= 7.5) &
    (df['imdb_votes'] >= 10000)
][['title_x', 'year_of_release', 'imdb_rating', 'imdb_votes']])
print(
    df[df['imdb_votes'] >= 5000]
    .nlargest(20, 'imdb_rating')
    [['title_x', 'imdb_rating', 'imdb_votes']]
)
avg_rating = df.groupby('year_of_release')['imdb_rating'].mean()
print(avg_rating)
print("Highest average rating year:",
      avg_rating.idxmax())
print("Highest average rating:",
      avg_rating.max())
import numpy as np
rating_norm = (
    (df['imdb_rating'] - df['imdb_rating'].min()) /
    (df['imdb_rating'].max() - df['imdb_rating'].min())
)
log_votes = np.log1p(df['imdb_votes'])
votes_norm = (
    (log_votes - log_votes.min()) /
    (log_votes.max() - log_votes.min())
)
df['combined_score'] = (rating_norm + votes_norm) / 2
print(
    df.nlargest(10, 'combined_score')
    [['title_x', 'imdb_rating', 'imdb_votes', 'combined_score']]
)
df['primary_genre'] = df['genres'].str.split('|').str[0]
print(df[['title_x', 'genres', 'primary_genre']])
genre = df.groupby('primary_genre').agg(
    movie_count=('title_x', 'count'),
    average_rating=('imdb_rating', 'mean')
)
print(
    genre.sort_values(
        ['movie_count', 'average_rating'],
        ascending=False
    ).head(5)
)
print(
    df[
        df['tagline'].isnull() &
        (df['imdb_rating'] > 7.0)
    ][['title_x', 'imdb_rating']]
)
final_df = df[
    ['title_x',
     'year_of_release',
     'primary_genre',
     'imdb_rating',
     'imdb_votes']
]
final_df = final_df.sort_values(
    ['imdb_rating', 'imdb_votes'],
    ascending=[False, False]
)
print(final_df)