import re
from pathlib import Path


class Directory:
    def __init__(self, path, parent):
        self.path = path
        self.parent = parent
        self.sub_directories = {}
        self.files = {}

    def add_file(self, file):
        self.files[file.name] = file

    def create_child_dir(self, path):
        if self.path == '/':
            self.sub_directories[path] = Directory(f'/{path}', self)
        else:
            self.sub_directories[path] = Directory(f'{self.path}/{path}', self)

    def total_size(self):
        file_sizes = sum(file.size for file in self.files.values())
        subdir_sizes = sum(subdir.total_size() for subdir in self.sub_directories.values())
        return file_sizes + subdir_sizes

    def cd(self, subdir):
        if subdir == '..':
            return self.parent
        return self.sub_directories[subdir]

    def subdirs(self):
        return self.sub_directories.values()

    def total_under_size(self, n):
        subdirs_under_size = sum(d.total_under_size(n) for d in self.subdirs())
        if self.total_size() <= n:
            return self.total_size() + subdirs_under_size
        return subdirs_under_size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def total_size(self):
        return self.size


def read_input():
    p = Path(__file__).with_name("day07.txt")
    with p.open() as f:
        return [line.strip() for line in f.readlines()]


def generate_filesystem(lines):
    root_dir = Directory('/', parent=None)
    current_dir = root_dir

    cd_pattern = re.compile('\$ cd (.+)')
    file_pattern = re.compile('(\d+) (.+)')
    dir_pattern = re.compile('dir (.+)')

    for line in lines:
        if cd_match := cd_pattern.findall(line):
            current_dir = current_dir.cd(cd_match[0])
        elif file_match := file_pattern.findall(line):
            file_size, file_name = int(file_match[0][0]), file_match[0][1]
            current_dir.add_file(File(file_name, file_size))
        elif dir_match := dir_pattern.findall(line):
            current_dir.create_child_dir(dir_match[0])

    return root_dir


inp = read_input()[1:]
root_directory = generate_filesystem(inp)

TOTAL_DISK_SPACE = 70000000
REQUIRED_UNUSED_SPACE = 30000000
used_space = root_directory.total_size()
currently_unused_space = TOTAL_DISK_SPACE - used_space

directories_by_size = []
stack = [root_directory]
while stack:
    dir_to_check = stack.pop()
    directories_by_size.append(dir_to_check.total_size())
    stack.extend(dir_to_check.subdirs())

smallest_size_to_delete = next(size for size in sorted(directories_by_size)
                               if currently_unused_space + size > REQUIRED_UNUSED_SPACE)

print(f"Part 1 answer: {root_directory.total_under_size(100000)}")
print(f"Part 2 answer: {smallest_size_to_delete}")
