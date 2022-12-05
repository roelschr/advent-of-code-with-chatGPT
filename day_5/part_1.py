import re

def rearrange_crates(stacks, instructions):
    # Compile regular expression to match instructions
    pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")

    # Iterate through instructions
    for instruction in instructions.strip().split("\n"):
        # Match instruction to regular expression
        match = pattern.match(instruction)

        # Retrieve instruction components
        quantity, from_stack, to_stack = match.groups()

        # Retrieve the crates to move
        crates = stacks[int(from_stack) - 1][-int(quantity):]

        # Remove crates from the "from" stack
        stacks[int(from_stack) - 1] = stacks[int(from_stack) - 1][:-int(quantity)]

        # Reverse the order of the crates and add them to the "to" stack
        stacks[int(to_stack) - 1].extend(reversed(crates))

    # Return the top crate of each stack
    return "".join([stack[-1] for stack in stacks])

# Open input file
with open("input.txt") as file:
    # Read file contents
    contents = file.read()

    # Split file contents into stacks and instructions
    stacks, instructions = contents.split("\n\n", maxsplit=1)

    # Parse stacks
    stacks = [list(line) for line in stacks.split("\n")]
    stacks = [list(reversed(line)) for line in zip(*stacks)]
    stacks = [re.findall(r"[A-Z]", "".join(line)) for line in stacks if line[0].isdigit()]

    # Rearrange crates
    result = rearrange_crates(stacks, instructions)

    # Print result
    print(result)
