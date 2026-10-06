# Import the math module.
import math

# Create a list of product prices.
prices = [199.1, 349.8, 599.3]

# Round each price up to the nearest whole number.
rounded_prices = [math.ceil(price) for price in prices]

# Display the rounded prices.
print("Rounded prices:", rounded_prices)