# Define a function that takes video titles and view counts.
def get_rounded_views(titles, view_counts):

    # Pair each title with its view count and round the count to the nearest thousand.
    result = [(title, round(views, -3)) for title, views in zip(titles, view_counts)]

    # Return the list of tuples.
    return result


# Create a list of YouTube video titles.
titles = [
    "Python Basics",
    "Django Tutorial",
    "HTML CSS Project",
    "Python API Tutorial"
]

# Create a list of view counts.
view_counts = [12500, 34780, 8920, 156430]

# Call the function and store the returned result.
rounded_views = get_rounded_views(titles, view_counts)

# Display the list of tuples.
print("Rounded video views:", rounded_views)