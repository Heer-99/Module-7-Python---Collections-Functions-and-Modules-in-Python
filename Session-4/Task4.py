# Create a mixed tuple containing different types of data.
insta_post = (
    101,
    "tech_world",
    1250,
    ["python", "coding", "developer"],
    True
)

# Display the complete tuple.
print("Instagram Post:", insta_post)

# Display the type of each element.
print("Type of post_id:", type(insta_post[0]))
print("Type of username:", type(insta_post[1]))
print("Type of likes:", type(insta_post[2]))
print("Type of hashtags:", type(insta_post[3]))
print("Type of is_public:", type(insta_post[4]))