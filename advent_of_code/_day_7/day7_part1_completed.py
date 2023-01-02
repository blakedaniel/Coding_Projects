
file = 'GitHub/Coding_Projects/advent_of_code/_day_7/input_part1.txt'
data = open(file)


input_lines = []
for line in data:
    line = line.strip()
    if not line.startswith('$ ls'):
        input_lines.append(line.split())


class Content():
    def __init__(self, term_direct):
        self.terminal_contents = term_direct[0]
        self.directories = term_direct[1]
        self.above_100000 = {}
        self.total_space = 70000000
        self.available_space = 0
        self.required_space = 30000000


def concat_lst(lst):
    string = ''
    for n in lst:
        # n = n + '_'
        string += n
    return string


def pathifyDirect(lsts):
    path = []
    directories = []
    for line in lsts:
        if len(line) == 3:  # either setting a new directory or moving up a directory
            if line[2] == '..':  # moving up a directory
                path.pop()
                directory_path = concat_lst(path)
            else:  # setting a new directory
                path.append(line[2])
                directory_path = concat_lst(path)
                line[2] = directory_path
                directories.append(directory_path)
        else:  # contents of a directory
            if line[0].isnumeric():  # file_size, file_name
                pass
            elif line[0] == 'dir':  # dir, directory_name
                line[1] = f'{directory_path}{line[1]}'
    return (lsts, directories)


def identfiyDirectSize(direct_path='/', lsts=[]):
    i = lsts.index(['$', 'cd', direct_path])
    size = 0
    for line in lsts[i + 1:]:
        if line[0:2] == ['$', 'cd']:
            return size
        elif line[0].isnumeric():
            size += int(line[0])
        elif line[0] == 'dir':
            size += identfiyDirectSize(line[1], lsts)
    return size


contents = Content(pathifyDirect(input_lines))
total = 0

for directory in contents.directories:
    size = identfiyDirectSize(directory, contents.terminal_contents)
    if size <= 100000:
        print(directory, size)
        total += size
total
