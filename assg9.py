import pandas as pd
df=pd.read_csv(r"C:\Users\muska\OneDrive\muskan csf pdf\movies (2).csv")
df['genres'] = df['genres'].fillna('Unknown')
print(df['genres'].isnull().sum())
genre = df['genres'].str.split('|').explode()
print(genre.value_counts())
df['genre'] = df['genres'].str.split('|')
genre_df = df.explode('genre')
print(
    genre_df.groupby('genre')[['imdb_rating', 'imdb_votes']].mean()
)
genre_stats = genre_df.groupby('genre').agg(
    movie_count=('title_x', 'count'),
    average_rating=('imdb_rating', 'mean')
)
print(
    genre_stats[
        (genre_stats['movie_count'] >= 30) &
        (genre_stats['average_rating'] >= 6.5)
    ]
)
top10_genres = genre_stats.nlargest(10, 'movie_count').index

result = genre_df[genre_df['genre'].isin(top10_genres)]

print(
    result.loc[
        result.groupby('genre')['imdb_rating'].idxmax()
    ][['genre', 'title_x', 'imdb_rating']]
)
print(
    genre_df.groupby('genre')['imdb_votes']
    .mean()
    .sort_values(ascending=False)
    .head(1)
)
df['period'] = df['year_of_release'].apply(
    lambda x: 'Before 2010' if x < 2010 else '2010 onwards'
)

print(
    df.groupby('period').agg(
        average_rating=('imdb_rating', 'mean'),
        average_votes=('imdb_votes', 'mean'),
        number_of_movies=('title_x', 'count')
    )
)
avg_rating = df['imdb_rating'].mean()
median_votes = df['imdb_votes'].median()

print(
    df[
        (df['imdb_rating'] > avg_rating) &
        (df['imdb_votes'] > median_votes)
    ]
    .nlargest(10, 'imdb_rating')
    [['title_x', 'imdb_rating', 'imdb_votes']]
)
def rating_category(rating):
    if rating >= 8:
        return 'Outstanding'
    elif rating >= 7:
        return 'Very Good'
    elif rating >= 6:
        return 'Good'
    else:
        return 'Average'

df['rating_category'] = df['imdb_rating'].apply(rating_category)

print(df[['title_x', 'imdb_rating', 'rating_category']])
summary = df.groupby('rating_category').agg(
    number_of_movies=('title_x', 'count'),
    average_rating=('imdb_rating', 'mean')
)

print(summary)