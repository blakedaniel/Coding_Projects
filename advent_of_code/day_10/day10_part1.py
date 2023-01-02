file = 'GitHub/Coding_Projects/advent_of_code/day_10/test_input_part1.txt'
data = open(file)


class Cpu():
    def __init__(self):
        self.cycle = 1
        self.total_cyc = 0
        self.value = 1
        self.cyc_val = []
        self.signal_strg = 0

    def addx(self, value, cycle):
        self.cyc_val.append((cycle + 3, int(value)))
        return

    def execute(self, cur_cycle):
        for pair in enumerate(self.cyc_val): # take cycle and value pair from list of cyc_val pairings
            i = pair[0]
            pair = pair[1]
            c, v = pair
            if int(c) == cur_cycle:  # if there's a pairing where the trigger cycle is equal to current cycle
                cv = self.cyc_val.pop(i)  # remove this pairing from the list, set as pair variable
                self.value += cv[1]  # add the value from the CV pair, to the instance value


cpu = Cpu()
commands = []

for command in data:
    command = command.splitlines()[0]
    commands.append(command)
    cpu.total_cyc += 1

for i in range(1, cpu.total_cyc + 1):
    cpu.cycle = i
    command = commands[cpu.cycle - 1]
    print(cpu.cycle, cpu.value, command)
    if command.startswith('noob'):
        continue
    elif command.startswith('addx'):
        func, value = command.split()
        # print(value, cpu.cycle)
        cpu.addx(value, cpu.cycle)
    if cpu.cycle != 20:
        cpu.execute(cpu.cycle)
    elif cpu.cycle == 20:
        cpu.signal_strg = cpu.value * cpu.cycle
        break

