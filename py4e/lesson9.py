"""
# if-else loop version
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
"""
"""
# get beats if-else
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)
"""

# assigment
name = input("Enter file:")
dict = {}
emails = []
lrgst_cnt = 0
lrgst_email = None

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if not line.startswith('From:'):
        continue
    lst = line.split()
    email = lst[1]
    dict[email] = dict.get(email, 0) + 1
    if dict[email] > lrgst_cnt:
        lrgst_cnt = dict[email]
        lrgst_email = email

print('First code:', lrgst_email, lrgst_cnt)

# assignment answer 2

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = {}

for line in handle:
    if not line.startswith('From:'):
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

lrgst_email = None
lrgst_cnt = None

for email, count in counts.items():
    if lrgst_cnt is None or count > lrgst_cnt:
        lrgst_email = email
        lrgst_cnt = count

print('second code:', lrgst_email, lrgst_cnt)
