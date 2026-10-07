# Import add_to_cart directly from the shoppingcart package.
from shoppingcart import add_to_cart

cart = []

# Add an item to the shopping cart.
cart = add_to_cart("Laptop", cart)

print("Cart:", cart)
