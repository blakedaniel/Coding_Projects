file = 'GitHub/Coding_Projects/advent_of_code/_day_11/input_part1.txt'
data = open(file)


class Monkey():
    def __init__(self, name):
        self.name = name
        self.items = []
        self.operation = []
        self.divis = 0
        self.t_monkey = ''
        self.f_monkey = ''
        self.activity = 0


def monkey_profiles():
    monkeys = []
    for line in data:
        line = line.strip()
        if line.startswith('Monkey'):
            name = line.removesuffix(':').lower()
            monkey = Monkey(name)
        elif line.startswith('Starting items: '):
            items = line.removeprefix('Starting items: ')
            items = items.split(', ')
            for i, item in enumerate(items):
                items[i] = int(item)
            monkey.items = items
        elif line.startswith('Operation: new = '):
            operation = line.removeprefix('Operation: new = ')
            operation = operation.split()
            monkey.operation = operation
        elif line.startswith('Test'):
            divis = line.removeprefix('Test: divisible by ')
            divis = int(divis)
            monkey.divis = divis
        elif line.startswith('If true'):
            t_monkey = line.removeprefix('If true: throw to monkey ')
            monkey.t_monkey = int(t_monkey)
        elif line.startswith('If false'):
            f_monkey = line.removeprefix('If false: throw to monkey ')
            monkey.f_monkey = int(f_monkey)
            if monkey not in monkeys:
                monkeys.append(monkey)
    return monkeys


monkeys = monkey_profiles()


def mod_adjust(num):
    mods = [monkey.divis for monkey in monkeys]
    sup_mod = 1
    for mod in mods:
        sup_mod *= mod
    num = num % sup_mod
    return num


def monkey_operator(item, operation=[]):
    num1 = operation[0]
    num2 = operation[2]
    operator = operation[1]
    if num1 == 'old':
        num1 = item
    if num2 == 'old':
        num2 = item
    else:
        num2 = int(num2)
    if operator == '*':
        ans = num1 * num2
    elif operator == '+':
        ans = num1 + num2
    elif operator == '-':
        ans = num1 - num2
    elif operator == '/':
        ans = num1 / num2
    return ans


n = 10000
while n != 0:
    for monkey in monkeys:
        monkey.activity += len(monkey.items)
        for i, item in enumerate(monkey.items):
            item = mod_adjust(item)
            monkey.items[i] = monkey_operator(item, monkey.operation)
            if monkey.items[i] % monkey.divis == 0:
                monkeys[monkey.t_monkey].items.append(monkey.items[i])
            else:
                monkeys[monkey.f_monkey].items.append(monkey.items[i])
        monkey.items = []
    n -= 1


top_two = [monkey.activity for monkey in monkeys]
top_two.sort(reverse=True)
print(top_two[0]*top_two[1])
