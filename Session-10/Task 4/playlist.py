# Add a song to the playlist.
def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist


# Remove a song if it exists in the playlist.
def remove_song(song_name, playlist):
    if song_name in playlist:
        playlist.remove(song_name)
    return playlist


# Display each song with its position number.
def display_playlist(playlist):
    for position, song in enumerate(playlist, start=1):
        print(position, "-", song)