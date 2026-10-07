# Test script for instahelpers.format_likes

from instahelpers import format_likes

# Test various like counts
counts = [500, 999, 1000, 1200, 1500, 10000, 999999, 1500000, 2500000]

for count in counts:
    print(f"{count} -> {format_likes(count)}")
