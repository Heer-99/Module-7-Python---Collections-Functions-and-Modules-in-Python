# Create a list of IPL team names.
teams = ["CSK", "MI", "GT", "RCB", "KKR"]

# Create a list of their total points.
points = [12, 8, 14, 16, 10]

# Use zip() to create a dictionary.
team_points = dict(zip(teams, points))

# Print teams that have more than 10 points.
for team, point in team_points.items():
    if point > 10:
        print(team, "-", point, "points")