# Create a lambda function to return sum and product.
calculate = lambda a, b: (a + b, a * b)

# Process the given pairs.
pairs = [(3, 4), (5, 2), (7, 8)]

# Print the sum and product for each pair.
for a, b in pairs:
    result = calculate(a, b)
    print("Pair:", (a, b), "Sum:", result[0], "Product:", result[1])