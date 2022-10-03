"""
# sorting by value in a dictionary or tuple
c = {'a': 10, 'b': 1, 'c': 22}
tmp = []
for (key, value) in c.items():
    tmp.append((value, key))
print('Non-Sorted')
print(tmp)

tmp = sorted(tmp, reverse=True)
print('Sorted')
print(tmp)

print(sorted([(v, k) for k, v in c.items()]))
"""

# exersice
# open file for analysis
fname = input('Enter File Name:')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)

# create dictionary of word frequency
di = dict()
for lin in hand:
    # print(lin)
    lin = lin.rstrip()
    # print(lin)
    wrd = lin.split()
    # print(wrd)
    for w in wrd:
        # print(w)
        di[w] = di.get(w, 0) + 1
        # print(di)
print('Dictionary:', di)

# create sortable list from dictionary
tmp = []
print(dir(tmp))
for k, v in di.items():
    print(k, v)
    tmp = tmp.append(v, k)
    print(tmp)

"""
# assignment
# get file
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = {}

# create count dictionary of times in a day
for line in handle:
    if not line.startswith('From '):
        continue
    tmp = line.split()
    # print(tmp)
    tmp = tmp[5].split(':')
    # print(tmp)
    count[tmp[0]] = count.get(tmp[0], 0) + 1
    # print(count)

# create and print sorted list based off of count values in dictionary
for key, value in sorted(count.items()):
    print(key, value)
"""
