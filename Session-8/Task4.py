# Define a function to apply a coupon discount.
def apply_coupon(amount, coupon_code=None):
    # Apply a 10% discount if the coupon code is SAVE10.
    if coupon_code == "SAVE10":
        amount = amount - (amount * 10 / 100)

    # Return the final amount.
    return amount


# Test without passing the coupon code.
print("Final amount:", apply_coupon(1000))


# Test by passing the coupon code.
print("Final amount:", apply_coupon(1000, "SAVE10"))