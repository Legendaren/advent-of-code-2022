def read_input():
    with open("day02.txt") as file:
        file_lines = [line.rstrip().split() for line in file]
        return file_lines


rounds = read_input()


# Part 1

def char_to_score(char):
    char_to_score_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    return char_to_score_dict[char]


def round_score(you, opponent):
    score = {
        'X': {'A': 3, 'B': 0, 'C': 6},
        'Y': {'A': 6, 'B': 3, 'C': 0},
        'Z': {'A': 0, 'B': 6, 'C': 3},
        'A': {'A': 3, 'B': 0, 'C': 6},
        'B': {'A': 6, 'B': 3, 'C': 0},
        'C': {'A': 0, 'B': 6, 'C': 3}
    }
    return score[you][opponent]


def round_points(your_play, opponents_play):
    return round_score(your_play, opponents_play) + char_to_score(your_play)


total_points = sum(round_points(your_char, opponent_char) for opponent_char, your_char in rounds)
print(f"Part 1 answer: {total_points}")


# Part 2
def matching_char(you, opponent):
    matching_char = {
        'X': {'A': 'C', 'B': 'A', 'C': 'B'},
        'Y': {'A': 'A', 'B': 'B', 'C': 'C'},
        'Z': {'A': 'B', 'B': 'C', 'C': 'A'},
    }
    return matching_char[you][opponent]


converted_rounds = [[o, matching_char(y, o)] for o, y in rounds]
total_points_converted = sum(round_points(your_char, opponent_char) for opponent_char, your_char in converted_rounds)
print(f"Part 2 answer: {total_points_converted}")
