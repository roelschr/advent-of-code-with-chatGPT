def find_start_of_packet(data):
    # Keep track of the last four characters received
    last_four = []

    # Loop through the data, one character at a time
    for i, ch in enumerate(data):
        # Add the current character to the list of last four
        last_four.append(ch)
        # If the list has more than four characters, remove the first one
        if len(last_four) > 4:
            last_four = last_four[1:]

        # Check if the last four characters are all different
        if len(set(last_four)) == 4:
            # Return the number of characters processed so far
            return i + 1

# Read the data from stdin
data = input()

# Find the start of the packet and print the result
print(find_start_of_packet(data))
