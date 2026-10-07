# Create an empty dictionary for playlists
playlists = {}


# Create a function to add a song to a user's playlist
def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):

    # Create the user if the user does not exist
    if user not in playlists:
        playlists[user] = {}

    # Create the playlist if the playlist does not exist
    if playlist_name not in playlists[user]:
        playlists[user][playlist_name] = []

    # Create a dictionary for the song details
    song = {
        "song_title": song_title,
        "artist": artist
    }

    # Add the song to the playlist
    playlists[user][playlist_name].append(song)


# Add the first song
add_song_to_playlist(
    playlists,
    "user1",
    "Chill Songs",
    "Varoon Forever",
    "Aditya Gadhvi"
)

# Add the second song
add_song_to_playlist(
    playlists,
    "user1",
    "Chill Songs",
    "Sanson Ki Mala",
    "Various Artist"
)

# Add the third song to a new playlist
add_song_to_playlist(
    playlists,
    "user1",
    "Gujarati Songs",
    "Vhalam Aavo Ne",
    "Various Artist"
)

# Add the fourth song for a new user
add_song_to_playlist(
    playlists,
    "user2",
    "My Favorites",
    "Dhun Lagi",
    "Various Artist"
)


# Print the complete playlists
print(playlists)