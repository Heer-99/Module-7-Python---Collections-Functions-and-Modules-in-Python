# Create a list containing multiple playlists with song durations
playlists = [[210, 180, 240], [150, 200], [300, 120, 90]]

# Create a new list with durations greater than 200 seconds
durations = [
    duration
    for playlist in playlists
    for duration in playlist
    if duration > 200
]

# Print the durations greater than 200 seconds
print(durations)