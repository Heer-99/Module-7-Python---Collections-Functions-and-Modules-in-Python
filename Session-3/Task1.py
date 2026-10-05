# Create a list of cricket scores with decimal values.
scores = [56.7, 102.3, 88.9, 45.2, 120.8]

# Create an empty list to store the rounded scores.
rounded_scores = []

# Round each score to the nearest integer and add it to the new list.
for score in scores:
    rounded_scores.append(round(score))

# Print the original list.
print("Original scores:", scores)

# Print the rounded list.
print("Rounded scores:", rounded_scores)