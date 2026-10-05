# Create the nested dictionary for IPL teams.
team = {
    "CSK": {
        "captain": "Dhoni",
        "players": 18
    },
    "MI": {
        "captain": "Rohit",
        "players": 17
    }
}

# Add a new team GT with its captain and number of players.
team["GT"] = {
    "captain": "Hardik",
    "players": 16
}

# Print all team names and their captains.
for team_name in team:
    print(team_name, "-", team[team_name]["captain"])