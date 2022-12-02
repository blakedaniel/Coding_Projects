# day1.py

file = 'advent_of_code/day_1/input_part1.txt'
fhand = open(file)


def mostCalories(data):
    max_cal = 0
    cur_cal = 0

    for line in fhand:
        l = line.rstrip()

        if l.isnumeric():
            cur_cal += int(l)
        else:
            if cur_cal > max_cal:
                max_cal = cur_cal
            cur_cal = 0

    return max_cal


mostCalories(fhand)
