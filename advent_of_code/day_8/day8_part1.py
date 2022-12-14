file = 'GitHub/Coding_Projects/advent_of_code/day_8/test_input_part1.txt'
data = open(file)
data = list(data.read().splitlines())

class Tree():
    def __init__(self, height=0, row=0, col=0):
        self.height = int(height)
        self.row = int(row)
        self.col = int(col)
        self.location = (self.row, self.col)
        self.sightLines = {'row': [], 'col': []}
        self.visible = True

    def __repr__(self):
        return f'({self.height}, {self.row}, {self.col})'


# make columns based on column position of tree
def makeColumn(data, col):
    column = []
    for line in data:
        line = line.strip()
        line = list(line)
        column.append(line[col])
    return column

def makeRow(line):
    for item in line:
        item = line.pop(0)
        item = int(item)
        line.append(item)
    return line

cur_tree = Tree(3, 2, 2)
cur_tree.sightLines['row'] = [6, 5, 3, 3, 2]
cur_tree.sightLines['col'] = [7, 1, 3, 4, 9]

def visibilityCheck(cur_tree=Tree(0, 0, 0)):
    if cur_tree.col in (0, len(cur_tree.sightLines['col'])-1):
        return True
    elif cur_tree.row in (0, len(cur_tree.sightLines['row'])-1):
        return True
    else:
        dimensions = tuple(cur_tree.sightLines.keys())
        for dimension in dimensions:
            if dimension == 'row':
                index_check = cur_tree.row
            if dimension == 'col':
                index_check = cur_tree.col
            other_trees = cur_tree.sightLines[dimension]
            other_trees.pop(index_check)
            for tree in other_trees:
                if cur_tree.height >= int(tree):
                    return True
    return False

# create instances of all possible trees based on Tree class and data
def curTree(data):
    row = -1
    for line in data:
        line = line.strip()
        row += 1
        col = -1
        for tree in line:
            tree = int(tree)
            col += 1
            cur_tree = Tree(tree, row, col)
            cur_tree.sightLines['row'] = makeRow(list(line))
            cur_tree.sightLines['col'] = makeColumn(data, col)
            cur_tree.visible = visibilityCheck(cur_tree)
            yield cur_tree  # change to yeild when ready to officially use


current_trees = curTree(data)

count = 0
for tree in current_trees:
    if tree.col not in (0, 4) and tree.row not in (0, 4):
        count += 1
        print(tree, tree.sightLines, count)
