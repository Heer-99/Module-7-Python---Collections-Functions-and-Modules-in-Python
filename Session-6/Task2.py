# Create a list of Instagram usernames.
usernames = ["raj_07", "ananya_xo", "coder_21", "nidhi_99"]

# Create a list of follower counts.
follower_counts = [1200, 2500, 980, 1750]

# Create an empty dictionary.
followers = {}

# Use a loop to add each username and follower count to the dictionary.
for i in range(len(usernames)):
    followers[usernames[i]] = follower_counts[i]

# Display the dictionary.
print("Instagram followers:", followers)