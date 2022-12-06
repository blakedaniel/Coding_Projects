
# tried = WFCGHBJZF
# tried = WFCBHBJGC

file = 'GitHub/Coding_Projects/advent_of_code/day_5/input_part1.txt'
data = open(file)
current_stacks = data.read(324)  # should be 324 for full text, 48 for test cases
print(current_stacks)

stacks = {}
for stack in range(1, 10):  # change end number to 10 for full text, 4 for test cases
    stacks[stack] = []

count = 2
for chr in current_stacks:
    count += 1
    if chr.isalpha():
        stacks[count / 4].append(chr)

    if chr == '\n':
        # print(count)  # 36 chrs per line
        count = 2

for line in data:
    line = line.strip()
    if line.startswith('move'):
        move = line.split()
        count = 0
        num = int(move[1]) - 1
        from_stack = int(move[3])
        to_stack = int(move[5])
        while num >= 0:
            crate = stacks[from_stack].pop(num)
            stacks[to_stack].insert(0, crate)
            num -= 1

top = ''
for v in stacks.values():
    top += v[0]

print(top)
