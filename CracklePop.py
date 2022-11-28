# CracklePop.py

def snapCracklePop():
    for num in range(1, 101):
        if num % 15 == 0:
            print('CracklePop')
        elif num % 5 == 0:
            print('Pop')
        elif num % 3 == 0:
            print('Crackle')
        else:
            print(num)

snapCracklePop()