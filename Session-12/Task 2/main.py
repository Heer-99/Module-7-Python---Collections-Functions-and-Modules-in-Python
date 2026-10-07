# Import both functions directly from the foodorder package.
from foodorder import get_menu, place_order

# Get and display the menu.
menu = get_menu()
print("Menu:", menu)

# Place an order.
place_order("Pizza")
