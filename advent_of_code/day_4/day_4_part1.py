
data = '''
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''

file = 'GitHub/Coding_Projects/advent_of_code/day_4/input_part1.py'
data = open(file)


count = 0
for pairs in data:  # remove split when ready for full data
    pair = pairs.partition(',')
    ass1 = pair[0].split('-')
    ass2 = pair[2].split('-')
    ass1 = set(range(int(ass1[0]), int(ass1[1]) + 1))
    ass2 = set(range(int(ass2[0]), int(ass2[1]) + 1))
    if ass1.issubset(ass2) or ass2.issubset(ass1):
        count += 1

print(count)