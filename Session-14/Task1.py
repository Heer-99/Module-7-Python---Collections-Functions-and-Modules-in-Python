# Create an empty dictionary for the Flipkart shopping cart
shopping_cart = {}

# Add the first user to the shopping cart
shopping_cart["user1"] = {}

# Add two items for the first user
shopping_cart["user1"]["item1"] = {
    "name": "Shoes",
    "quantity": 2,
    "price": 1500
}

shopping_cart["user1"]["item2"] = {
    "name": "Bag",
    "quantity": 1,
    "price": 1200
}

# Add the second user to the shopping cart
shopping_cart["user2"] = {}

# Add two items for the second user
shopping_cart["user2"]["item1"] = {
    "name": "Watch",
    "quantity": 1,
    "price": 2500
}

shopping_cart["user2"]["item2"] = {
    "name": "Headphones",
    "quantity": 2,
    "price": 2200
}

# Print the entire shopping cart
print(shopping_cart)