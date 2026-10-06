# Import the required functions from playlist.py.
from playlist import add_song, remove_song

# Create an empty playlist.
playlist = []

# Add three songs to the playlist.
playlist = add_song("Varoon Forever", playlist)
playlist = add_song("Vhalam Aavo Ne", playlist)
playlist = add_song("Sanson Ki Mala", playlist)

# Remove 'Shape of You' from the playlist.
playlist = remove_song("Vhalam Aavo Ne", playlist)

# Print the updated playlist.
print("Updated playlist:", playlist)