# instahelpers package
# Provides a function to format like counts similar to Instagram.

def format_likes(count):
    """Format a like count as Instagram-style K/M notation."""
    if count < 1000:
        return count
    elif count < 1_000_000:
        return f"{count / 1000:.1f}K"
    else:
        return f"{count / 1_000_000:.1f}M"
