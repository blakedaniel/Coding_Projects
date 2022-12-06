file = 'GitHub/Coding_Projects/advent_of_code/day_4/input_part1.py'
data = open(file)


count = 0
for pairs in data:  # remove split when ready for full data
    pair = pairs.partition(',')
    ass1 = pair[0].split('-')
    ass2 = pair[2].split('-')
    ass1 = set(range(int(ass1[0]), int(ass1[1]) + 1))
    ass2 = set(range(int(ass2[0]), int(ass2[1]) + 1))
    if len(ass1.intersection(ass2)) > 0:
        count += 1

print(count)