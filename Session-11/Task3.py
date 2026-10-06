# Import the math module.
import math

# Set the order bill amount.
bill_amount = 1250.75

# Apply a 10% discount.
discounted_amount = bill_amount - (bill_amount * 10 / 100)

# Round down the final bill to the nearest rupee.
final_bill = math.floor(discounted_amount)

# Display the final bill amount.
print("Final bill amount:", final_bill)