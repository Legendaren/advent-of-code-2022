def read_input():
    with open("day06.txt") as file:
        return file.readlines()[0].rstrip()


def first_pos_where_all_chars_differ(buffer, char_count):
    start_index = char_count - 1
    for i in range(start_index, len(buffer)):
        last_char_count_chars = buffer[i - start_index:i + 1]
        if len(set(last_char_count_chars)) == len(last_char_count_chars):
            return i + 1
    return None


input_buffer = read_input()
print(f"Part 1 answer: {first_pos_where_all_chars_differ(input_buffer, 4)}")
print(f"Part 2 answer: {first_pos_where_all_chars_differ(input_buffer, 14)}")
