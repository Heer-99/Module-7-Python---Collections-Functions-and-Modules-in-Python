# Create a matrix containing ratings for 3 Zomato restaurants
ratings = [
    [4, 5, 3, 2],
    [5, 4, 4, 3],
    [3, 2, 5, 5]
]

# Find ratings above 4 and flatten them into a single list
high_ratings = [
    rating
    for row in ratings
    for rating in row
    if rating > 4
]

# Print the ratings above 4
print(high_ratings)