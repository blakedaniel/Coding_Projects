
file = 'GitHub/Coding_Projects/advent_of_code/day_5/input_part1.txt'
data = open(file)
current_stacks = data.read(324)

stacks = {}
for stack in range(1, 10):
    stacks[stack] = []

count = 2
for chr in current_stacks:
    count += 1
    if chr.isalpha():
        stacks[count / 4].append(chr)

    if chr == '\n':
        count = 2


for line in data:
    line = line.strip()
    if line.startswith('move'):
        move = line.split()
        count = 0
        num = int(move[1])
        from_stack = int(move[3])
        to_stack = int(move[5])
        while count < num:
            crate = stacks[from_stack].pop(0)
            stacks[to_stack].insert(0, crate)
            count += 1

top = ''
for v in stacks.values():
    top += v[0]

print(top)
