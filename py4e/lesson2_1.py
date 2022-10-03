# increment
# n = n + 1

# random d6
# random('7 digit number') % 6

# first program
# inp = input('Europe floor?')
# usf = int(inp) + 1
# print('US floor', usf)

# chapter 4: Functions

# functions and conditionals if, elif, else
def greet(lang):
    if lang == 'en':
        print('hello')
    elif lang == 'es':
        print('hola')
    else:
        print('bonjour')


greet('es')

# function with return values


def greet2():
    return ('Hello')


print(greet2(), 'Blake')
print(greet2(), 'Mikaela')

# interations and loops
# while loops blastoff
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!!')


# break and continue

while True:
    line = raw_input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# for loops

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')


# Functions assignment (Pay 498.75)

def computepay(h, r):
    if h > 40:
        pay = (40 * r) + ((h-40) * (1.5 * r))
    else:
        pay = (40 * r)
    return pay


hrs = input("Enter Hours:")
hrs = float(hrs)
rt = input('Enter Pay Rate:')
rt = float(rt)
p = computepay(hrs, rt)
print("Pay", p)


# loops
while True:
    line = input('>>> ')
    if line[0] == '#':
        continue  # continue back to the top of the while statement on line 83
    if line == 'done':
        break  # ends the current loop and jumps to the statement immediately following the loop

    print(line)
print('Done!')


# largest number

largest = None
nums = [7, 2, 'bob', 10, 4]
for num in nums:
    try:
        float(num)
        if largest is None:
            largest = num
            print(largest, num)
        elif largest < num:
            largest = num
            print(largest, num)
    except Exception:
        print(num, 'is not an integer, please update.')


print('largest number is', largest)

# smallest number
smallest = None
nums = [7, 2, 'bob', 10, 4]
for num in nums:
    try:
        float(num)
        if ((smallest is None) or (smallest > num)):
            smallest = num
            print(smallest, num)
    except Exception:
        print(num, 'is not an integer, please update.')


print('smallest number is', smallest)


# variation of smallest search, user input
smallest = None
while True:
    num = input('Enter Number or "done"')
    print('smallest:', smallest, '| num:', num)
    if num == 'done':
        break
    try:
        int(num)
        num = int(num)
        if (smallest is None) or (smallest > num):
            smallest = num
    except Exception:
        print(num, 'is not an integer, please update.')

print('smallest number is', smallest)


# loop assignment [7, 2, 'bob', 10, 4, 'done']

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    print(num)
    try:
        int(num)
        num = int(num)
        if (smallest is None) or (smallest > num):
            smallest = num
        if (largest is None) or (largest < num):
            largest = num
    except Exception:
        print('Invalid input')


print('Maximum', largest)
print('Minimum', smallest)

# strings

for letter in 'banana':
    print(letter)

word = 'banana'
n = -1
while n < len(word):
    n = n + 1
    print(word[n])


print('Blake Van Fleteren'.lower)
name = 'Blake Van Fleteren'
print(name.lower)
dir(name)  # gives all the methods that can be applied to the name variable

# common methods
str = 'heath is crying, but hes fine'

str.find('is')  # position of the first instance of 'is' in str
ispos = str.find('is')
str.find('h', ispos)  # find the first 'h' after the first 'is' (posis)

str.lower()  # lower cases the string str
str.upper()  # upper cases the string str
str.replace('is', 'was')  # replaces all instances of 'is' with 'was'
str.lstrip()  # removes all white space LEFT of the first character in the string
str.rstrip()  # removes all white space RIGHT of the first character in the string
str.strip()  # removes all white space RIGHT and LEFT of the first character in the string

# string assignment
# pull out the number and turn it into a float and print
text = "X-DSPAM-Confidence:    0.8475"
lspos = text.find(' ')
num = text[lspos:]
num = float(num.lstrip())
print(num)


# file management in python
fhandle = open('filename'. mode)  # this is the HANDLE, not the file itself

# new line can be executed with \n and is considered whitespace
# searching through a file (without loading the entire file)
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()  # strips the "from" lines of whitespace, and the newlines
    if line.startswith('From:'):  # searches for lines that start with 'From:'
        print(line)


# files section
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
print("Done")
