
file = 'GitHub/Coding_Projects/advent_of_code/day_3/input_part1.py'
rucksacks = open(file)

priority_sum = 0


for rucksack in rucksacks:
    rucksack = rucksack.rstrip()
    length = int(len(rucksack))
    half = int(len(rucksack)/2)
    capart1 = set(rucksack[0:half])
    capart2 = set(rucksack[half:length])
    type = capart1.intersection((capart2)).pop()
    if type.islower():
        priority = ord(type) - 96
    elif type.isupper():
        priority = ord(type) - 38
    priority_sum += priority

print(priority_sum)
