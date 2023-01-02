file = 'GitHub/Coding_Projects/advent_of_code/day_10/input_part1.txt'
data = open(file)

commands = []
for command in data:
    command = command.splitlines()[0]
    commands.append(command)


def listReplace(lst=[], org=0, new='#'):
    i = lst.index(org)
    lst.remove(org)
    lst.insert(i, new)


class Cpu():
    def __init__(self):
        self.pixel = 0
        self.x = 1
        self.pixels = []
        self.brk = 40

    @property
    def sprite(self):
        s = (self.x - 1, self.x, self.x + 1)
        return s

    @property
    def cur_brk_pnt(self):
        mult = int((self.pixel / self.brk) + 1)
        cbp = self.brk * mult
        return cbp

    def displayPixels(self, lst=[], start=0, end=1):
        n_rows = (end - start) // self.brk
        n_tail = end % self.brk
        if n_tail != 0:
            n_rows += 1

        r_end = self.brk

        while n_rows != 0:
            print(*lst[start:r_end])
            start += self.brk
            r_end += self.brk
            n_rows -= 1

    def startingPixels(self):
        for n in range(0, 241):
            self.pixels.append(n)

    def spriteCheck(self, pixel=0, sprite=(-1, 0, 1)):
        if pixel in sprite:
            listReplace(self.pixels, pixel, '#')
        else:
            listReplace(self.pixels, pixel, '.')

    def updateRowX(self):
        if self.pixel % self.brk == 0:
            self.x += self.brk

    def noop(self):
        self.spriteCheck(self.pixel, self.sprite)
        self.displayPixels(self.pixels, 0, self.pixel + 1)
        display_test()
        self.pixel += 1
        self.updateRowX()

    def addx(self, value):
        self.spriteCheck(self.pixel, self.sprite)
        self.displayPixels(self.pixels, 0, self.pixel + 1)
        display_test()
        self.pixel += 1
        self.updateRowX()
        self.spriteCheck(self.pixel, self.sprite)
        self.displayPixels(self.pixels, 0, self.pixel + 1)
        display_test()
        self.x += value
        self.pixel += 1
        self.updateRowX()



cpu = Cpu()
cpu.startingPixels()


def display_test():
    br = '---------------------'
    c = ('COMMAND:', command)
    p = ('PIXEL:', cpu.pixel)
    s = ('SPRITE:', cpu.sprite)
    rb = ('ROW BREAK:', cpu.cur_brk_pnt)
    x = ('X:', cpu.x)
    test_msg = f'{br}\n {c}\n {p}\n {s}\n {x}\n {rb}\n {br}'
    print(test_msg)


for command in commands[:]:
    if command.startswith('addx'):
        cpu.addx(int(command.split()[1]))
    else:
        cpu.noop()
