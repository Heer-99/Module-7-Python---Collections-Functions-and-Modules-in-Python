# Create a list of Flipkart product names
names = ['Shoes', 'Bag', 'Watch', 'Headphones']

# Create a list of product prices
prices = [999, 1500, 700, 2200]

# Create tuples for products with prices above 1000
products = [
    (name, price)
    for name, price in zip(names, prices)
    if price > 1000
]

# Print the final list of products
print(products)