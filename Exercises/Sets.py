def main():
    # Take two lists as input from the user
    list1 = input("Enter the first list of elements separated by spaces: ").split()
    list2 = input("Enter the second list of elements separated by spaces: ").split()

    # Convert lists to sets
    set1 = set(list1)
    set2 = set(list2)

    # Find common elements
    common_elements = set1.intersection(set2)

    # Display the common elements
    print("Common elements between the two lists are:", common_elements)

main()

# Create a set named colors containing the specified items
colors = {"red", "green", "blue", "yellow"}

# Print the set
print(colors)

# Add the color "purple" to the colors set
colors.add("purple")

# Remove the color "green" from the set
colors.discard("green")

# Print the updated set
print(colors)

# Create a set named primary_colors containing the specified items
primary_colors = {"red", "blue", "yellow"}

# Find and print the colors that are in colors but not in primary_colors
print("Colors in colors but not in primary_colors:", colors.difference(primary_colors))

# Find and print the colors that are in both colors and primary_colors
print("Colors in both colors and primary_colors:", colors.intersection(primary_colors))

# Check membership and print an appropriate message
if "orange" in colors:
    print("Orange is in the colors set.")
else:
    print("Orange is not in the colors set.")