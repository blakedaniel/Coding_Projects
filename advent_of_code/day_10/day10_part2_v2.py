
import itertools

file = 'GitHub/Coding_Projects/advent_of_code/day_10/test_input_part1.txt'
data = open(file)

commands = []
for line in data:
    line = line.split()
    commands.append(line)

print(commands)

class Screen():
    def __init__(self):
        self.cur_pixel = 1
        self.prev_x = 0
        self.cur_x = 1
        self.pixels = []

    @property
    def cur_sprite(self):
        s = (self.cur_x - 1, self.cur_x, self.cur_x + 1)
        return s

    @property
    def prev_sprite(self):
        s = (self.prev_x - 1, self.prev_x, self.prev_x + 1)
        return s

    def startingPixels(self):
        for n in range(1, 241):
            self.pixels.append(n)
        return


screen = Screen()
screen.startingPixels()


def addx(command):
    screen.prev_x = screen.cur_x
    screen.cur_x += int(command[1])
    return


def listReplace(lst=[], org=0, new='#'):
    i = lst.index(org)
    lst.remove(org)
    lst.insert(i, new)


def holidayMessage():
    for command in commands:
        print(screen.pixels)
        if command[0].startswith('noop'):
            screen.cur_pixel += 1
            continue
        else:
            screen.cur_pixel += 2
            # print(command)
            addx(command)
            if screen.prev_x in screen.prev_sprite:
                print(screen.prev_sprite)
                listReplace(screen.pixels, screen.prev_x, '#')
            elif screen.cur_x in screen.cur_sprite:
                listReplace(screen.pixels, screen.cur_x, '#')


holidayMessage()
