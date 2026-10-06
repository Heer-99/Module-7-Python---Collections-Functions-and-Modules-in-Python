# Import the random module.
import random

# Create a list of 8 songs.
songs = [
    "Varoon Forever",
    "Sanson Ki Mala",
    "Saavariya",
    "Dhun Lagi",
    "Vhalam Aavo Ne",
    "Rang Morla",
    "Radha Ne Shyam Mali Jashe",
    "Chand Ne Kaho"
]

# Select 3 random songs for today's playlist.
daily_playlist = random.sample(songs, 3)

# Print today's playlist.
print("Today's playlist:", daily_playlist)