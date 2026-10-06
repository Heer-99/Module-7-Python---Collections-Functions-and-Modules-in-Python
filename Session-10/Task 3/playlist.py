# Define a function to add a song to the playlist.
def add_song(song_name, playlist):
    # Add the song to the playlist.
    playlist.append(song_name)

    # Return the updated playlist.
    return playlist


# Define a function to remove a song from the playlist.
def remove_song(song_name, playlist):
    # Remove the song if it exists in the playlist.
    if song_name in playlist:
        playlist.remove(song_name)

    # Return the updated playlist.
    return playlist