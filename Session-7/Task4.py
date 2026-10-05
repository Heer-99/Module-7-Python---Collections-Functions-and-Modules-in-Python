# Define a function to count word frequency while ignoring stopwords.
def word_freq_dict(text):
    # Create a list of common stopwords.
    stopwords = ["the", "and", "in", "of", "a", "to", "is"]

    # Convert the text to lowercase.
    text = text.lower()

    # Remove punctuation.
    text = text.replace(",", "").replace(".", "")

    # Split the text into individual words.
    words = text.split()

    # Create an empty dictionary.
    word_count = {}

    # Count words that are not stopwords.
    for word in words:
        if word not in stopwords:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Return the word frequency dictionary.
    return word_count


# Create a sample text.
text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"

# Display the word frequency dictionary.
print(word_freq_dict(text))