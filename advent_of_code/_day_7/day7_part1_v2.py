
import re

file = 'GitHub/Coding_Projects/advent_of_code/day_7/test_input_part1.txt'
data = open(file)
# data = data.read()


class File():
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.parent = ''

    def __repr__(self):
        return '({}, {})'.format(self.name, self.size)


class Directory():
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.contents = {'folders': [], 'files': []}
        self.parent = ''

    def __repr__(self):
        return '({}, {})'.format(self.name, self.size)


def content_search(folder_name):
    folder = Directory(folder_name)
    # print(folder, folder.contents)
    for line in data:
        line = line.strip()
        if line.startswith('dir'):
            sub_folder_name = line.removeprefix('dir ')
            sub_folder = Directory(sub_folder_name)
            folder.contents['folders'].append(sub_folder)
            # print(folder, folder.contents)
        elif re.search('[0-9]', line):
            size, name = line.split(' ')
            file = File(name)
            file.parent = folder.name
            file.size = int(size)
            folder.contents['files'].append(file)
            folder.size += file.size
            # print(folder, folder.contents)
        elif re.fullmatch('^\$ cd \w', line):
            pat = re.search(('(\$ cd )(\w)'), line)
            sub_folder_name = pat.group(2)
            sub_folder = Directory(sub_folder_name)
            # print(type(sub_folder), type(folder.contents['folders'][0]), 'print')
            # folder.contents['folders'].remove(sub_folder)
            sub_folder = content_search(sub_folder_name)
            folder.contents['folders'].append(sub_folder)
            folder.size += sub_folder.size
            print(folder, folder.contents)
        elif line == '$ cd ..':
            return folder
    return folder


content_search('/')
