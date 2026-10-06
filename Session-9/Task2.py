# Create a list of food item prices.
prices = [120, 250, 99, 180, 310]

# Add a 10% service charge using lambda and map().
updated_prices = list(map(lambda price: price + (price * 10 / 100), prices))

# Print the updated prices.
print("Updated prices:", updated_prices)