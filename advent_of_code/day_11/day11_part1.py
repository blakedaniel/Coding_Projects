file = 'GitHub/Coding_Projects/advent_of_code/_day_11/input_part1.txt'
data = open(file)

monkeys = {}
for line in data:
    line = line.strip()
    if line.startswith('Monkey'):
        monkey = line.removesuffix(':').lower()
        monkeys[monkey] = {
            'cur_items': [],
            'prev_items': [],
            'activity': 0
        }
    elif line.startswith('Starting'):
        starting_items = line.removeprefix('Starting items: ')
        starting_items = starting_items.split(', ')
        for n in range(0, len(starting_items)):
            starting_items[n] = int(starting_items[n])
        monkeys[monkey]['cur_items'] = starting_items

# need to update this so that list is being updated


def monkey_operation(name):
    items = monkeys[name]['cur_items']
    monkeys[name]['activity'] += len(items)
    match name:
        case 'monkey 0':
            for item in items:
                item = items.pop()
                item *= 2
                items.append(item)
        case 'monkey 1':
            for item in items:
                item = items.pop()
                item += 3
                items.append(item)
        case 'monkey 2':
            for item in items:
                item = items.pop()
                item += 6
                items.append(item)
        case 'monkey 3':
            for item in items:
                item = items.pop()
                item += 5
                items.append(item)
        case 'monkey 4':
            for item in items:
                item = items.pop()
                item += 8
                items.append(item)
        case 'monkey 5':
            for item in items:
                item = items.pop()
                item *= 5
                items.append(item)
        case 'monkey 6':
            for item in items:
                item = items.pop()
                item = item
                items.append(item)
        case 'monkey 7':
            for item in items:
                item = items.pop()
                item += 4
                items.append(item)


def test(item, divs, t_monkey, f_monkey):
    if item % divs == 0:
        monkeys[t_monkey]['cur_items'].append(item)
    else:
        monkeys[f_monkey]['cur_items'].append(item)


def monkey_move(name):
    match name:
        case 'monkey 0':
            monkeys[name]['prev_items'] = monkeys[name]['cur_items']
            monkeys[name]['cur_items'] = []
            items = monkeys[name]['prev_items']
            for item in items:
                test(item, 17, 'monkey 2', 'monkey 5')
        case 'monkey 1':
            monkeys[name]['prev_items'] = monkeys[name]['cur_items']
            monkeys[name]['cur_items'] = []
            items = monkeys[name]['prev_items']
            for item in items:
                test(item, 13, 'monkey 7', 'monkey 4')
        case 'monkey 2':
            monkeys[name]['prev_items'] = monkeys[name]['cur_items']
            monkeys[name]['cur_items'] = []
            items = monkeys[name]['prev_items']
            for item in items:
                test(item, 19, 'monkey 6', 'monkey 5')
        case 'monkey 3':
            monkeys[name]['prev_items'] = monkeys[name]['cur_items']
            monkeys[name]['cur_items'] = []
            items = monkeys[name]['prev_items']
            for item in items:
                test(item, 7, 'monkey 7', 'monkey 1')
        case 'monkey 4':
            monkeys[name]['prev_items'] = monkeys[name]['cur_items']
            monkeys[name]['cur_items'] = []
            items = monkeys[name]['prev_items']
            for item in items:
                test(item, 11, 'monkey 0', 'monkey 2')
        case 'monkey 5':
            monkeys[name]['prev_items'] = monkeys[name]['cur_items']
            monkeys[name]['cur_items'] = []
            items = monkeys[name]['prev_items']
            for item in items:
                test(item, 3, 'monkey 6', 'monkey 3')
        case 'monkey 6':
            monkeys[name]['prev_items'] = monkeys[name]['cur_items']
            monkeys[name]['cur_items'] = []
            items = monkeys[name]['prev_items']
            for item in items:
                test(item, 2, 'monkey 3', 'monkey 1')
        case 'monkey 7':
            monkeys[name]['prev_items'] = monkeys[name]['cur_items']
            monkeys[name]['cur_items'] = []
            items = monkeys[name]['prev_items']
            for item in items:
                test(item, 5, 'monkey 4', 'monkey 0')


n = 20
activities = []
while n != 0:
    for name in monkeys.keys():
        monkey_operation(name)
        monkey_move(name)
    n -= 1

for name in monkeys.keys():
    activity = monkeys[name]['activity']
    activities.append(activity)

activities.sort(reverse=True)
top_two = activities[:2]

monkey_business_level = top_two[0] * top_two[1]
print(monkey_business_level)


# incorrect guesses: (14399639972, too low), (14395919064)
