# Create a list of usernames with their follower counts.
users = [('nidhi', 800), ('khushi', 1500), ('dhruvi', 1200), ('vamika', 950)]

# Filter users with more than 1000 followers.
k_badge_users = list(filter(lambda user: user[1] > 1000, users))

# Print the usernames that would get the K badge.
for user in k_badge_users:
    print(user[0])