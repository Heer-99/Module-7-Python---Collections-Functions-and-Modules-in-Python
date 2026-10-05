# Create a tuple containing the food order.
order = ('Burger', 'Fries', 'Coke')

# Convert the tuple into a list.
order_list = list(order)

# Add 'Ice Cream' to the end of the list.
order_list.append('Ice Cream')

# Convert the list back into a tuple.
order = tuple(order_list)

# Display the final tuple.
print("Final order:", order)