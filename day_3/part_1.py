# Function to convert a character to its priority value
def char_to_priority(c):
    if c.islower():
        # Lowercase letters have priorities 1-26
        return ord(c) - ord('a') + 1
    elif c.isupper():
        # Uppercase letters have priorities 27-52
        return ord(c) - ord('A') + 27

# Read rucksack contents from standard input
rucksacks = []
while True:
    try:
        line = input()
    except EOFError:
        # Stop reading when end of file is reached
        break
    rucksacks.append(line)

# Initialize total priority to 0
total_priority = 0

# Loop through each rucksack
for rucksack in rucksacks:
    # Get the first and second compartment of the rucksack
    first_compartment = rucksack[:len(rucksack) // 2]
    second_compartment = rucksack[len(rucksack) // 2:]

    # Initialize set of common items to the intersection of the two compartments
    common_items = set(first_compartment) & set(second_compartment)

    # Loop through each common item
    for item in common_items:
        # Convert the item to its priority value and add it to the total priority
        total_priority += char_to_priority(item)

# Print the total priority
print(total_priority)
