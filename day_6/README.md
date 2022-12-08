# Day 6: Tuning Trouble

### Prompt:

Hi, I have a puzzle for you! Please, give me a solution in Python 3 and code explanation.

The preparations are finally complete; you and the Elves leave camp on foot and begin to make your way toward the star fruit grove.

As you move through the dense undergrowth, one of the Elves gives you a handheld device. He says that it has many fancy features, but the most important one to set up right now is the communication system.

However, because he's heard you have significant experience dealing with signal-based systems, he convinced the other Elves that it would be okay to give you their one malfunctioning device - surely you'll have no problem fixing it.

As if inspired by comedic timing, the device emits a few colorful sparks.

To be able to communicate with the Elves, the device needs to lock on to their signal. The signal is a series of seemingly-random characters that the device receives one at a time.

To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet marker in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four characters that are all different.

The device will send your subroutine a datastream buffer (your puzzle input); your subroutine needs to identify the first position where the four most recently received characters were all different. Specifically, it needs to report the number of characters from the beginning of the buffer to the end of the first such four-character marker.

For example, suppose you receive the following datastream buffer:

`mjqjpqmgbljsphdztnvjfqwrcgsmlb`

After the first three characters (mjq) have been received, there haven't been enough characters received yet to find the marker. The first time a marker could occur is after the fourth character is received, making the most recent four characters mjqj. Because j is repeated, this isn't a marker.

The first time a marker appears is after the seventh character arrives. Once it does, the last four characters received are jpqm, which are all different. In this case, your subroutine should report the value 7, because the first start-of-packet marker is complete after 7 characters have been processed.

Here are a few more examples:

`bvwbjplbgvbhsrlpgdmjqwftvncz`: first marker after character 5
`nppdvjthqldpwncqszvftbrmjlhg`: first marker after character 6
`nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg`: first marker after character 10
`zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`: first marker after character 11

How many characters need to be processed before the first start-of-packet marker is detected?

### Answer:

To solve this problem, we can keep track of the last four characters received and check if they are all different. If they are, then we have found the start of the packet and can return the number of characters processed so far.

Here is the code in Python 3:

```python
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

# Test the function
print(find_start_of_packet("mjqjpqmgbljsphdztnvjfqwrcgsmlb")) # should print 7
print(find_start_of_packet("bvwbjplbgvbhsrlpgdmjqwftvncz")) # should print 5
print(find_start_of_packet("nppdvjthqldpwncqszvftbrmjlhg")) # should print 6
print(find_start_of_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")) # should print 10
print(find_start_of_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")) # should print 11
```

The find_start_of_packet function takes a string of data as input and returns the number of characters that need to be processed before the first start-of-packet marker is detected. It maintains a list of the last four characters received and loops through the data, adding each character to the list and removing the first one if necessary. If the list of last four characters contains only unique characters, then it means that we have found the start of the packet and the function returns the number of characters processed so far.


### Prompt:
Great, can you change the code to read the input from stdin?

Sure, here is the updated code that reads the input from stdin and prints the result to stdout:

```python
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
```

To use this code, you can save it to a file (e.g. solution.py) and run it like this:

```shell
python solution.py < input.txt
```

where input.txt is the file containing the input data. The result will be printed to stdout.


### Prompt:

Perfect, but consider this follow-up question:

Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

`mjqjpqmgbljsphdztnvjfqwrcgsmlb`: first marker after character 19
`bvwbjplbgvbhsrlpgdmjqwftvncz`: first marker after character 23
`nppdvjthqldpwncqszvftbrmjlhg`: first marker after character 23
`nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg`: first marker after character 29
`zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`: first marker after character 26
How many characters need to be processed before the first start-of-message marker is detected?

To solve this problem, we can modify the find_start_of_packet function to take an optional parameter for the number of distinct characters to look for. The default value for this parameter is 4, which means that the function will look for a start-of-packet marker. If we set this parameter to 14, then the function will look for a start-of-message marker instead.

Here is the updated code in Python 3:

```python
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
```

To use this code, you can save it to a file (e.g. solution.py) and run it like this:

```shell
python solution.py < input.txt
```

where input.txt is the file containing the input data. The result will be printed to stdout, first the number of characters needed to find the start of the packet and then the number of characters needed to find the start of the message.