# Create an empty dictionary to store IPL team scores
ipl_scores = {}

# Add RCB with three players and their runs
ipl_scores["RCB"] = {
    "Virat Kohli": 75,
    "Rajat Patidar": 45,
    "Jitesh Sharma": 32
}

# Add GT with three players and their runs
ipl_scores["GT"] = {
    "Shubman Gill": 82,
    "Jos Buttler": 65,
    "Rashid Khan": 28
}

# Print the runs scored by a specific player
print("Virat Kohli scored:", ipl_scores["RCB"]["Virat Kohli"], "runs")