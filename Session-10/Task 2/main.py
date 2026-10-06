# Import the add_song function from playlist.py.
from playlist import add_song

# Create an empty playlist.
playlist = []

# Add three songs to the playlist.
playlist = add_song("Varoon Forever", playlist)
playlist = add_song("Sanson ki Mala", playlist)
playlist = add_song("Vhalam Aavo Ne", playlist)

# Print the final playlist.
print("Final playlist:", playlist)