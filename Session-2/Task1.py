# Create a playlist containing five favorite song names.
playlist = [
    "Vhalam Aavo Ne",
    "Varoon Forever",
    "Sanson ki Mala",
    "Dhun Lagi",
    "Radha ne Shyam Mali Jashe"
]

# Use a for loop to print each song with its position.
for position in range(len(playlist)):
    print(position + 1, "-", playlist[position])