# Take a multi-line review from the user.
review = input("Enter your review: ")

# Convert the review to lowercase.
review = review.lower()

# Remove common punctuation marks.
for punctuation in ".,!?":
    review = review.replace(punctuation, "")

# Split the review into individual words.
words = review.split()

# Create an empty dictionary to store word frequencies.
word_count = {}

# Count each word.
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the word frequency dictionary.
print("Word frequency:", word_count)