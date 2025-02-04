"""
This program:
- Sorts the names in alphabetical order.
- Removes any duplicates.
- Displays the final sorted list.
"""

# Prompt the user for input
names_input = input("Enter a list of names, separated with commas: ")

# Convert input to a list, strip spaces, remove duplicates using set, then back to a sorted list
names_list = list(set(name.strip() for name in names_input.split(',')))

# Sort the names alphabetically
names_list.sort()

# Display the sorted unique names
print("\nSorted unique names:")
for name in names_list:
    print(name)

# Print the total number of unique names
print(f"\nTotal number of unique names: {len(names_list)}")  # Fixed 'Len' to 'len'
