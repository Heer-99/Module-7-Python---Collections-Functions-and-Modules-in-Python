# Create a list of product names.
products = ["iPhone 17", "OnePlus 15R", "AirPods", "Power Bank"]

# Create a list of product prices.
prices = [79999, 45999, 12999, 1999]

# Use zip() to create a dictionary from both lists.
product_prices = dict(zip(products, prices))

# Display the dictionary.
print("Product prices:", product_prices)