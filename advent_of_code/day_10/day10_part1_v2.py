file = 'GitHub/Coding_Projects/advent_of_code/day_10/input_part1.txt'
data = open(file)


class Cpu():
    def __init__(self):
        self.cycle = 1
        self.value = 1
        self.prev_value = 0
        self.signal_strg = 0

    def addx(self, value, cycle):
        self.cycle += 2
        self.prev_value = self.value
        self.value += int(value)
        return

    def noop(self, cycle):
        self.cycle += 1
        return


cpu = Cpu()


report_cycle = 20
for command in data:
    command = command.split()
    if command[0] == 'noop':
        cpu.noop(cpu.cycle)
    elif command[0] == 'addx':
        cpu.addx(command[1], cpu.cycle)
    if cpu.cycle == report_cycle + 1:
        cpu.signal_strg += (cpu.prev_value * report_cycle)
        report_cycle += 40
    elif cpu.cycle == report_cycle:
        cpu.signal_strg += (cpu.value * report_cycle)
        report_cycle += 40
