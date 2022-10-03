'''
# identifying the maxiumum spam confidence coefficient
import re
hand = open('mbox-short.txt')
numlist = []
for line in hand:
    line = line.rstrip()
    # print(line)
    confid = re.findall('^X-DSPAM-Confidence: ([^ ]+)', line)
    if len(confid) != 1:
        continue
    # print(confid, len(confid))
    confid = float(confid[0])
    # print(confid)
    numlist.append(confid)
    # print(numlist)
print('Maximum: ', max(numlist))
'''
# asignment
import re
# read the file
hand = open('regex_sum_42.txt')

# look for integers using re.findall(), and summing them
for line in hand:
    # print(line)
    num = re.findall('[0-9.]+', line)
    if len(num) == 0 or num[0] == '.':
        continue
    # print(num)
    for str in line:
        try:
