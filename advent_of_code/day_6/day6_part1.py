
file = 'GitHub/Coding_Projects/advent_of_code/day_6/input_part1.txt'
data = open(file)


def sniffPacket(signal, groups_of=4):
    count = 0
    i = 0
    for chr in signal:
        count += 1
        packet_marker = set()
        for n in tuple(range(i, i + groups_of)):
            packet_marker.add(signal[n])
        if len(packet_marker) == groups_of:
            return count + (groups_of - 1)
        else:
            i += 1


for line in data:
    sniffPacket(line.strip(), groups_of=4)
