# Define a function to count the frequency of each word.
def word_freq_dict(text):
    # Remove punctuation from the text.
    text = text.replace(",", "")

    # Split the text into individual words.
    words = text.split()

    # Create an empty dictionary.
    word_count = {}

    # Count each word.
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Return the word frequency dictionary.
    return word_count


# Store the given string.
text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"

# Call the function and display the result.
print(word_freq_dict(text))