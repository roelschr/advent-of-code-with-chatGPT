def find_start_of_packet(data, num_chars=4):
    # Keep track of the last `num_chars` characters received
    last_chars = []

    # Loop through the data, one character at a time
    for i, ch in enumerate(data):
        # Add the current character to the list of last `num_chars`
        last_chars.append(ch)
        # If the list has more than `num_chars` characters, remove the first one
        if len(last_chars) > num_chars:
            last_chars = last_chars[1:]

        # Check if the last `num_chars` characters are all different
        if len(set(last_chars)) == num_chars:
            # Return the number of characters processed so far
            return i + 1

# Read the data from stdin
data = input()

# Find the start of the packet and print the result
print(find_start_of_packet(data))

# Find the start of the message and print the result
print(find_start_of_packet(data, num_chars=14))
