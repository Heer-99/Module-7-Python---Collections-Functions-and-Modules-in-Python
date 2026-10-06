# Define a function to book a movie ticket.
def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    # Print the booking summary.
    print("Movie:", movie_name)
    print("Seat Type:", seat_type)
    print("Snacks:", snacks)
    print("--------------------")


# Call the function using only positional arguments.
book_movie_ticket("Jawan", "VIP", "Popcorn")


# Call the function using only keyword arguments.
book_movie_ticket(
    movie_name="Pathaan",
    seat_type="Premium",
    snacks="Nachos"
)


# Call the function using a mix of positional and keyword arguments.
book_movie_ticket("Jawan", snacks="Popcorn", seat_type="VIP")