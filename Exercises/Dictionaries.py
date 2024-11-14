# Dictionary with people and their favorite colors
favorite_colors = {
    "Ivan": "Red",
    "Kabi": "Blue",
    "Michelle": "Green"
}

# Print the dictionary
print(favorite_colors)

favorite_colors["David"] = "Yellow"

favorite_colors["Kabi"] = "Purple"

del favorite_colors["Michelle"]

if "Michelle" in favorite_colors:
    print("Michelle is in the dictionary.")
else:
    print("Michelle is not in the dictionary.")