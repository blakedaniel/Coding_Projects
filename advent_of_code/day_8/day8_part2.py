file = 'GitHub/Coding_Projects/advent_of_code/day_8/input_part1.txt'
data = open(file)
data = list(data.read().splitlines())


class Tree():
    def __init__(self, height=0, row=0, col=0):
        self.height = height
        self.loc = (row, col)
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.on_edge = False
        self.visible = False

    def __repr__(self):
        return f'({self.height}, {self.loc[0]}, {self.loc[1]})'


def rowsAndColumns(data):
    all_trees = {'rows': [], 'cols': []}
    all_rows = []
    all_columns = []
    for line in data:
        row = []
        for chr in line:
            num = int(chr)
            row.append(num)
        all_rows.append(row)
    row_leng = len(all_rows[0])
    for i in tuple(range(0, row_leng)):
        col = []
        for line in data:
            num = int(line[i])
            col.append(num)
        all_columns.append(col)
    all_trees['rows'] = all_rows
    all_trees['cols'] = all_columns
    return all_trees


all_trees = rowsAndColumns(data)


def edgeCheck(cur_tree=Tree(0, 0, 0)):
    if cur_tree.loc[0] in (0, len(all_trees['rows']) - 1):
        return True
    elif cur_tree.loc[1] in (0, len(all_trees['cols']) - 1):
        return True
    else:
        return False


def visibleCheck(cur_tree):
    if cur_tree.on_edge == True:
        return True
    else:
        sides = (cur_tree.left, cur_tree.right, cur_tree.up, cur_tree.down)
        side_checks = []
        for side in sides:
            side_checks.append(cur_tree.height > max(side))
        return True in side_checks



# create instances of all possible trees based on Tree class and data
def curTree(data):
    row = 0
    for line in data:
        col = 0
        for tree in line:
            # tree = tree
            cur_tree = Tree(tree, row, col)
            rows = all_trees['rows'][row]
            cur_tree.left = rows[:col]
            cur_tree.left.reverse()
            cur_tree.right = rows[col + 1:]
            cols = all_trees['cols'][col]
            cur_tree.up = cols[:row]
            cur_tree.up.reverse()
            cur_tree.down = cols[row + 1:]
            cur_tree.on_edge = edgeCheck(cur_tree)
            cur_tree.visible = visibleCheck(cur_tree)
            yield cur_tree  # change to yeild when ready to officially use
            col += 1
        row += 1


current_trees = curTree(all_trees['rows'])


def scenicScore(tree=Tree(0, 0, 0)):
    scenic_score = 1
    sides = (tree.up, tree.left, tree.down, tree.right)
    # print(sides)
    for side in sides:
        dist_to_edge = len(side)
        dist_to_tall = 0
        for side_tree in side:
            dist_to_tall += 1
            if side_tree >= tree.height:
                side_score = min(dist_to_edge, dist_to_tall)
                break
            elif side_tree < tree.height:
                side_score = dist_to_edge
                continue
        # print('SIDE SCORE:', side_score, 'TREE HEIGHT:', tree.height)
        scenic_score *= side_score
    return scenic_score


def highestScore():
    n = 0
    highest_score = 0
    for tree in current_trees:
        if tree.on_edge == False:
            n += 1
            if highest_score < scenicScore(tree):
                highest_score = scenicScore(tree)
    return highest_score

highestScore()