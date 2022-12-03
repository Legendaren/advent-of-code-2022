import string


def read_input():
    with open("day03.txt") as file:
        file_lines = [line.rstrip() for line in file]
        return file_lines

# Part 1
priority_dict = {}
priority_dict.update(dict((char, i) for i, char in enumerate(string.ascii_lowercase, start=1)))
priority_dict.update(dict((char, i) for i, char in enumerate(string.ascii_uppercase, start=27)))

rucksacks = read_input()
compartments_per_rucksack = [(line[:len(line) // 2], line[len(line) // 2:]) for line in rucksacks]
item_types_in_both_compartments = [
    next(iter(set(comp1).intersection(comp2))) for comp1, comp2 in compartments_per_rucksack
]
priority_sum = sum(priority_dict[item_type] for item_type in item_types_in_both_compartments)
print(f"Part 1 answer: {priority_sum}")

# Part 2
groups = [[rucksacks[j] for j in range(3*i, 3*i + 3)] for i in range(len(rucksacks) // 3)]
item_types_in_three_compartments = [
    next(iter(set.intersection(set(r1), set(r2), set(r3)))) for r1, r2, r3 in groups
]
badge_priority_sum = sum(priority_dict[item_type] for item_type in item_types_in_three_compartments)
print(f"Part 2 answer: {badge_priority_sum}")
