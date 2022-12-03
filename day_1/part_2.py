# Read the input data
data = []
while True:
    try:
        line = input().strip()
        if line:
            data.append(int(line))
        else:
            data.append(None)
    except EOFError:
        break

# Find the Elves with the most calories
elf_calories = {}
current_elf = None
for calories in data:
    if calories is not None:
        elf_calories[current_elf] = elf_calories.get(current_elf, 0) + calories
    else:
        current_elf = len(elf_calories)

# Sort the Elves by their total number of calories, in descending order
sorted_elves = sorted(elf_calories.items(), key=lambda x: x[1], reverse=True)

# Find the total number of calories carried by the top three Elves
top_3_calories = 0
for elf, calories in sorted_elves[:3]:
    top_3_calories += calories

# Print the result
print(top_3_calories)
