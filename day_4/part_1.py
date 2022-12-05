import re

# Parse the input into a list of tuples with the start and end values of each range
range_regex = re.compile(r"(\d+)-(\d+)")
ranges = [
    tuple(map(int, range_regex.match(pair).groups()))
    for line in open("input.txt")
    for pair in line.split(",")
]

# Zip the ranges into pairs of tuples
ranges = list(zip(ranges[::2], ranges[1::2]))

# Iterate over the ranges and check if one range fully contains the other
counter = 0
for range1, range2 in ranges:
    if (range1[0] <= range2[0] and range1[1] >= range2[1]) or (range2[0] <= range1[0] and range2[1] >= range1[1]):
        counter += 1

# Print the counter to get the solution to the puzzle
print(counter)
