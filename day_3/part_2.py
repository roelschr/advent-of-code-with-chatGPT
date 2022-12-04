from functools import reduce

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

# Group the rucksacks into sets of three
for i in range(0, len(rucksacks), 3):
    # Get the rucksacks in the current group
    group = rucksacks[i:i+3]

    # Use the reduce function to find the intersection of all three rucksacks in the group
    common_items = reduce(lambda a, b: set(a) & set(b), group)

    # Loop through each common item
    for item in common_items:
        # Convert the item to its priority value and add it to the total priority
        total_priority += char_to_priority(item)

# Print the total priority
print(total_priority)
