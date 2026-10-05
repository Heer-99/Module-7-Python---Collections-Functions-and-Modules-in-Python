# Create a list of Zomato restaurant names.
restaurants = ['Burger Hub', 'Pizza Point', 'Sushi House']

# Create a list of delivery times in minutes.
delivery_times = [30, 25, 40]

# Use zip() to pair each restaurant with its delivery time.
for restaurant, time in zip(restaurants, delivery_times):

    # Print each restaurant with its delivery time.
    print(restaurant, "-", time, "min")