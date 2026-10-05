# Define a function to count the frequency of each character.
def char_count_dict(text):
    # Create an empty dictionary to store character counts.
    char_count = {}

    # Go through each character in the text.
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Return the character frequency dictionary.
    return char_count


# Create a sample text.
text = "Hello World"

# Get the character frequency dictionary.
result = char_count_dict(text)

# Sort the dictionary by character and create a new dictionary.
sorted_result = dict(sorted(result.items()))

# Print the sorted dictionary.
print("Sorted character count:", sorted_result)