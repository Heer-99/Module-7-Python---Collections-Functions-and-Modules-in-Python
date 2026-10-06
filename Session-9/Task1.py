# Create a lambda function to calculate the square of a number.
square = lambda number: number * number

# Print the squares of numbers from 1 to 5.
for number in range(1, 6):
    print(number, "->", square(number))