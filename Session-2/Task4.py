# Create a list containing unread message counts for each chat.
unread_counts = [2, 0, 15, 120, 5]

# Use a for loop to check each unread message count.
for count in unread_counts:

    # Print '99+' when the count is greater than 99.
    if count > 99:
        print("99+")

    # Otherwise, print the actual unread message count.
    else:
        print(count)