# Day 4: Camp Cleanup

### Prompt:

Hi, I have a programming puzzle for you. I want the solution in Python 3, with code explanations, please. Let's try?

Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:
```
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
```
For the first few pairs, this list means:

- Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
- The Elves in the second pair were each assigned two sections.
- The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.

This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

```
.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
```

Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?

### Answer:

The first step is to parse the input and convert it into a list of tuples with the start and end values of each range. This can be done using a regular expression to match the range format, and then using the map function to convert the strings into integers.

Once we have the list of tuples, we can iterate over it and check if one range fully contains the other. This can be done by checking if the start and end values of one range are within the start and end values of the other range.

If we find a range that fully contains another, we can increment a counter to keep track of the number of pairs. Finally, we can print the counter to get the solution to the puzzle.

Here is the code in Python 3:

```python
import re

# Parse the input into a list of tuples with the start and end values of each range
range_regex = re.compile(r"(\d+)-(\d+)")
ranges = [
    tuple(map(int, range_regex.match(line).groups()))
    for line in open("input.txt")
]

# Iterate over the ranges and check if one range fully contains the other
counter = 0
for range1, range2 in ranges:
    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        counter += 1

# Print the counter to get the solution to the puzzle
print(counter)
```

### Prompt:

Great, but section assignments for each pair is in the form of `1-2,3-4`, meaning each section has two pairs. Can you fix that?


### Answer:

Yes, I can modify the regular expression to match the range format with two pairs, and then use the split function to split the pairs and the map function to convert the strings into integers.

Here is the updated code in Python 3:


```python
import re

# Parse the input into a list of tuples with the start and end values of each range
range_regex = re.compile(r"(\d+)-(\d+)")
ranges = [
    tuple(map(int, range_regex.match(pair).groups()))
    for line in open("input.txt")
    for pair in line.split(",")
]

# Iterate over the ranges and check if one range fully contains the other
counter = 0
for range1, range2 in ranges:
    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        counter += 1

# Print the counter to get the solution to the puzzle
print(counter)
```

### Prompt:

Great, you are almost there. Unfortunately you are create a flattened list of tuples, instead of a list of tuples of tuples. Each tuple inside the list represent a line, having two tuples (pair of sections). Can you change that?

### Answer:

Yes, I can modify the code to create a list of tuples of tuples, where each tuple represents a line and each sub-tuple represents a pair of sections.

To do this, I will change the list comprehension to create a list of tuples with the pairs of sections for each line, and then use the zip function to create the tuples of tuples.

Here is the updated code in Python 3:


```python
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
    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        counter += 1

# Print the counter to get the solution to the puzzle
print(counter)
```

### Prompt:

Amazing, finally, you have to consider that any of the ranges has to be fully contained on the other. Can you make the change?

### Answer:

Yes, I can modify the code to check if one range fully contains the other or if the other range fully contains the one. This can be done by using the or operator and reversing the range values in the second check.

Here is the updated code in Python 3:


```python
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
```

### Prompt:

Perfect, right on target. But I have a follow up:

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

### Answer:

To find the number of pairs that overlap at all, we can use the range function to generate the list of sections for each range and then use the intersection method to find the common elements.

If the intersection is not empty, it means that the ranges overlap, so we can increment a counter to keep track of the number of pairs that overlap.

Here is the updated code in Python 3:

```python
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

# Iterate over the ranges and check if they overlap
counter = 0
for range1, range2 in ranges:
    sections1 = set(range(range1[0], range1[1] + 1))
    sections2 = set(range(range2[0], range2[1] + 1))
    if sections1.intersection(sections2):
        counter += 1

# Print the counter to get the solution to the puzzle
print(counter)
```

### Prompt:

Wonderful, thank you! Talk to you soon for our next puzzle!

### Answer:

You're welcome, looking forward to the next puzzle!
