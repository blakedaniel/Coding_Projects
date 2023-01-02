
file = 'GitHub/Coding_Projects/advent_of_code/day_6/input_part1.txt'
data = open(file)


def sniffPacket(signal):
    count = 0
    i = 0
    for chr in signal:
        count += 1
        n1, n2, n3, n4 = signal[i:i + 4]  # this is the big learning, that I keep forgetting!!!
        packet_marker = {n1, n2, n3, n4}
        if len(packet_marker) == 4:
            return count + (4 - 1)
        else:
            i += 1


for line in data:
    sniffPacket(line.strip())