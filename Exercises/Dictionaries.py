# Dictionary with people and their favorite colors
favorite_colors = {
    "Ivan": "Red",
    "Kabi": "Blue",
    "Michelle": "Green"
}

# Print the dictionary
print(favorite_colors)

# Add a new person and their favorite color
favorite_colors["David"] = "Yellow"

# Update Kabi's favorite color
favorite_colors["Kabi"] = "Purple"

# Delete Someone in the dictionary
del favorite_colors["Michelle"]

# Check if someone is in the dictionary
if "Michelle" in favorite_colors:
    print("Michelle is in the dictionary.")
else:
    print("Michelle is not in the dictionary.")