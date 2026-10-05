# Take a string input from the user.
text = input("Enter a string: ")

# Create an empty dictionary to store character counts.
char_count = {}

# Count each character in the string.
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Display the character count dictionary.
print("Character count:", char_count)