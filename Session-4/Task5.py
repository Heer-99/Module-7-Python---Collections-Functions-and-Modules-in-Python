# Create a tuple containing 7 WhatsApp call durations in minutes.
call_durations = (12, 5, 0, 20, 7, 3, 15)

# Convert the tuple into a list.
call_list = list(call_durations)

# Keep only calls that are 5 minutes or longer.
call_list = [duration for duration in call_list if duration >= 5]

# Convert the filtered list back into a tuple.
call_durations = tuple(call_list)

# Display the final tuple.
print("Final call durations:", call_durations)