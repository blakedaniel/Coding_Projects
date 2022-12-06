# day_3_part2.py

file = 'GitHub/Coding_Projects/advent_of_code/day_3/input_part2.py'
groups = open(file)

group = []
badge_ids = []
priority_sum = 0
count = 0

for elf in groups:
    count += 1
    elf = elf.strip()
    group.append(set(elf))
    if count % 3 == 0:
        badge_id = group[0].intersection(group[1])
        badge_id = badge_id.intersection(group[2])
        badge_id = badge_id.pop()
        if badge_id.islower():
            print('lower', badge_id)
            priority = ord(badge_id) - 96
        elif badge_id.isupper():
            print('upper', badge_id)
            priority = ord(badge_id) - 38
        priority_sum += priority
        group.clear()


print(priority_sum)
