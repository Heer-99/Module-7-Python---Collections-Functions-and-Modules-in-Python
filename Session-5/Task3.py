# Create a nested dictionary for restaurant menus.
restaurant_menu = {
    "Pizza Palace": {
        "cuisine": "Italian",
        "rating": 4.2
    },
    "Dosa Corner": {
        "cuisine": "South Indian",
        "rating": 4.0
    }
}

# Update the rating of one restaurant.
restaurant_menu["Pizza Palace"]["rating"] = 4.5

# Display the updated dictionary.
print("Updated restaurant menu:", restaurant_menu)