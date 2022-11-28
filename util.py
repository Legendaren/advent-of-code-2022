def read_file_lines(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        return lines