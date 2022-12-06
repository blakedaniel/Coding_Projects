# day1_part2.py

file = 'GitHub/Coding_Projects/advent_of_code/day_1/input_part1.txt'
fhand = open(file)


def topThree(data):
    top_three_pack = [0, 0, 0]
    min_top_three = min(top_three_pack)
    cur_cal = 0

    for line in fhand:
        l = line.rstrip()

        if l.isnumeric():
            cur_cal += int(l)
            print(cur_cal)
        else:
            if cur_cal > min_top_three:
                top_three_pack.remove(min_top_three)
                top_three_pack.append(cur_cal)
            cur_cal = 0
    return top_three_pack


topThree(fhand)
