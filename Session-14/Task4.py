# Create an empty dictionary to store Zomato orders
orders = {}


# Create a function to add a new order
def add_order(orders, order_id, restaurant, items, total):

    # Create the order if the order ID does not exist
    order = orders.setdefault(order_id, {})

    # Add restaurant name to the order
    order["restaurant"] = restaurant

    # Add items to the order
    order["items"] = items

    # Add total amount to the order
    order["total"] = total


# Create a function to update the total of an existing order
def update_total(orders, order_id, new_total):

    # Update the total of the specified order
    if order_id in orders:
        orders[order_id]["total"] = new_total


# Add the first order
add_order(
    orders,
    101,
    "Spice Hub",
    ["Pizza", "Cold Drink"],
    500
)

# Add the second order
add_order(
    orders,
    102,
    "Burger House",
    ["Burger", "French Fries"],
    350
)

# Update the total of the first order
update_total(orders, 101, 600)

# Print the complete orders
print(orders)