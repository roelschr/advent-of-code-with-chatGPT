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

# Find the Elf with the most calories
elf_calories = {}
current_elf = None
for calories in data:
    if calories is not None:
        elf_calories[current_elf] = elf_calories.get(current_elf, 0) + calories
    else:
        current_elf = len(elf_calories)

# Print the result
print(max(elf_calories.values()))
