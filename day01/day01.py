
# Part 1
def read_input():
    with open("day01.txt") as file:
        file_lines = [int(line.rstrip() or 0) for line in file]
        return file_lines


lines = read_input()
calories_per_elf = []
item_calories = []
for item in lines:
    if item == 0:
        calories_per_elf.append(item_calories)
        item_calories = []
        continue
    item_calories.append(item)

total_calories_per_elf = [sum(calories) for calories in calories_per_elf]
print(f"Part 1 answer: {max(total_calories_per_elf)}")

# Part 2
top_3_total_calories = sum(sorted(total_calories_per_elf, reverse=True)[0:3])
print(f"Part 2 answer: {top_3_total_calories}")