# Import functions from playlist.py.
from playlist import add_song, remove_song, display_playlist

# Create an empty playlist.
playlist = []

# Add songs to the playlist.
add_song("Varoon Forever", playlist)
add_song("Vhalam Aavo Ne", playlist)
add_song("Sanson Ki Mala", playlist)

# Remove Shape of You.
remove_song("Vhalam Aavo Ne", playlist)

# Display the final playlist.
display_playlist(playlist)