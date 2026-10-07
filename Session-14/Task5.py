# Import defaultdict from collections
from collections import defaultdict


# Create a nested dictionary for users and playlists
playlists = defaultdict(lambda: defaultdict(list))

# Add the existing user's playlist
playlists["user1"]["Favourites"].extend(["Song1", "Song2"])

# Add a new song to a new user's new playlist
playlists["user2"]["Chill"].append("Song3")

# Print the complete playlists
print(dict(playlists))