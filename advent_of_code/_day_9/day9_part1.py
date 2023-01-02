file = '/Users/blakevanfleteren/Documents/Programs/GitHub/Coding_Projects/advent_of_code/day_9/test_input_part1.txt'
data = open(file)

class RopeHead:
    def __init__(self):
        self.location = (0, 0)  # current location of RopeHead
        self.prior_loc = {(0, 0)}  # set of locations RopeHead has been

    def addLoc(self, location):
        return self.prior_loc.add(location)

    # moving RopeHead based off of move inputs
    def makeMove(self, move):
        move = tuple(move.split())
        match move[0]:
            case 'U':
                self.location = (self.location[0], self.location[1] + int(move[1]))
            case 'R':
                self.location = (self.location[0] + int(move[1]), self.location[1])
            case 'D':
                self.location = (self.location[0], self.location[1] - int(move[1]))
            case 'L':
                self.location = (self.location[0] - int(move[1]), self.location[1])
        return self.prior_loc.add(self.location)


class RopeTail():
    def __init__(self):
        self.location = (0, 0)  # current location of RopeHead
        self.prior_loc = {(0, 0)}  # set of locations RopeHead has been
        self.traveled = 1
        self.clostest_dist = 0

    def makeMove(self, head_location):
        case1 = self.location[0] == head_location[0]
        case2 = self.location[1] == head_location[1]
        case3 = abs(self.location[0] - head_location[0]) == 1
        case4 = abs(self.location[1] - head_location[1]) == 1
        if (self.location[0], self.location[1]) in self.diag_locs.values():
            return
        elif (case1 or case2) or (case3 or case4):
            if (case1 or case2) and not(case3 or case4):
                pass
            for k, v in self.possible_locs.items():
                if move[0] == k:
                    self.location = v

    def addLoc(self, location):
        return self.prior_loc.add(location)

    @property
    def possible_locs(self):
        p_locations = {
            'D': (head.location[0], head.location[1] + 1),
            'L': (head.location[0] + 1, head.location[1]),
            'U': (head.location[0], head.location[1] - 1),
            'R': (head.location[0] - 1, head.location[1])
        }
        return p_locations

    @property
    def diag_locs(self):
        diags = {
            'd1': (head.location[0] - 1, head.location[1] + 1),
            'd2': (head.location[0] - 1, head.location[1] - 1),
            'd3': (head.location[0] + 1, head.location[1] + 1),
            'd4': (head.location[0] + 1, head.location[1] - 1)
        }
        return diags


head = RopeHead()
tail = RopeTail()

for move in data:
    print(move.strip())
    head.makeMove(move)
    print('HEAD:', head.location)
    tail.makeMove(head.location)
    print('TAIL:', tail.location)
    # print('TAIL TRAV:', tail.clostest_dist)
