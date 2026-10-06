# Create a lambda function to check whether a string is a palindrome.
is_palindrome = lambda text: text == text[::-1]

# Test the given strings.
print("madam:", is_palindrome("madam"))
print("python:", is_palindrome("python"))
print("noon:", is_palindrome("noon"))