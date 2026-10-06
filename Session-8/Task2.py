# Define a function with username and an optional prefix.
def format_username(username, prefix="user_"):
    # Add the prefix before the username.
    return prefix + username


# Test the function without providing the prefix.
result1 = format_username("nidhi")
print("Without prefix:", result1)


# Test the function by providing a custom prefix.
result2 = format_username("nidhi", "admin_")
print("With prefix:", result2)