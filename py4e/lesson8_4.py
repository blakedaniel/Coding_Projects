# fname = input("Enter file name: ")
fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    line = line.strip()
    words = line.split()
    for word in words:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
