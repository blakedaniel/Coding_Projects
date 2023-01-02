
a = list(range(1, 12))
a

for item in a:
    if item % 10 == 0:
        print(item)
        break
    print('-----> THIS IS A BREAK')
    for item in a:
        print(item)