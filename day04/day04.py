from pathlib import Path


def read_input():
    p = Path(__file__).with_name("day04.txt")
    with p.open() as f:
        file_lines = [line.rstrip() for line in f]
        return file_lines


section_assignments = read_input()

# Part 1
fully_containing_pairs = 0
for assignment in section_assignments:
    pair1, pair2 = assignment.split(",")
    pair1_low, pair1_high = map(int, pair1.split("-"))
    pair2_low, pair2_high = map(int, pair2.split("-"))
    if (pair1_low >= pair2_low and pair1_high <= pair2_high) or \
            (pair2_low >= pair1_low and pair2_high <= pair1_high):
        fully_containing_pairs += 1

print(f"Part 1 answer: {fully_containing_pairs}")

# Part 2
overlapping_pairs = 0
for assignment in section_assignments:
    pair1, pair2 = assignment.split(",")
    pair1_low, pair1_high = map(int, pair1.split("-"))
    pair2_low, pair2_high = map(int, pair2.split("-"))
    if (pair1_low <= pair2_low <= pair1_high or pair1_low <= pair2_high <= pair1_high) or \
            (pair2_low <= pair1_low <= pair2_high or pair2_low <= pair1_high <= pair2_high):
        overlapping_pairs += 1

print(f"Part 2 answer: {overlapping_pairs}")
