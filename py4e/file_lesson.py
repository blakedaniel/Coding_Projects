# Use the file name mbox-short.txt as the file name
fname = 'mbox-short.txt'
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    numpos_start = line.find('0')
    numpos_end = len(line)
    spam = float(line[numpos_start:numpos_end])
    count = count + 1
    total = total + spam
    average = total/count
print('Average spam confidence:', average)
