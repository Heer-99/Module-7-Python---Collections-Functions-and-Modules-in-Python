# Create a list of movie titles.
titles = ["Mirzapur", "Drishyam 3", "Jindagi Once More", "Spider-Man"]

# Create a list of movie genres.
genres = ["Crime", "Mystery", "Drama", "Action"]

# Create a list of movie ratings.
ratings = [4.5, 4.6, 4.2, 4.4]

# Use zip() to combine the three lists.
movies = [
    {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    for title, genre, rating in zip(titles, genres, ratings)
]

# Display the list of dictionaries.
print("Movie list:", movies)