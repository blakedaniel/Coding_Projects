file = 'GitHub/Coding_Projects/advent_of_code/day_11/test_input_part1.txt'
data = open(file)

monkeys = {}

for line in data:
    line = line.strip()
    line = line.lstrip()
    print(line)
    if line.startswith('Monkey'):
        features = {
            'items': [],
            'operation': None,
            'test': None,
            't_monkey': None,
            'f_monkey': None
        }
        monkey = line.removesuffix(':')
        monkeys[monkey] = monkeys.get(monkey, features)
    elif line.startswith('Starting'):
        starting_items = line.removeprefix('Starting items: ')
        starting_items = starting_items.split(', ')
        for item in starting_items:
            item = int(item)
        monkeys[monkey][items].append(starting_items)
    elif line.startswith('Operation'):
        pass
    elif line.startswith('Test'):
        # don't forget to divide by 3 before running test and rounded down to nearest integer
        pass
    elif line.startswith('If true'):
        pass
    elif line.startswith('If false'):
        pass
