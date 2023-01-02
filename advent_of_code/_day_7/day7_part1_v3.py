
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


def folder_search(folder_name='/'):
    cur_folder = Directory(folder_name)
    for line in data:
        line = line.strip()
        if not re.search(f'\$ cd {cur_folder.name}', line):
            continue
        else:
            for line in data:
                line = line.strip()
                # print('---->', line)
                if line.startswith('$ cd ..'):
                    break
                elif line.startswith('dir '):
                    sub_folder_name = line.removeprefix('dir ')
                    cur_folder.contents['folders'].append(sub_folder_name)
                elif re.search('[0-9]', line):
                    size, name = line.split()
                    file = File(name)
                    file.size = int(size)
                    cur_folder.size += file.size
                    cur_folder.contents['files'].append(file)
                elif line.startswith('$ cd '):
                    sub_search = re.search(('(\$ cd )(\w)'), line)
                    sub_folder_name = sub_search.group(2)
                    if sub_folder_name not in cur_folder.contents['folders']:
                        print(sub_folder_name)
                        print('dir file not included')
                        return cur_folder
                    else:
                        sub_folder = folder_search(sub_folder_name)
                        print('---->', sub_folder)
                        cur_folder.size += sub_folder.size
    return cur_folder


folder_search('a')
