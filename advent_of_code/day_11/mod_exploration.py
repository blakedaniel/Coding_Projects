
nums = [79, 98, 54, 65, 75, 74, 79, 60, 97, 74]

mods = [23, 19, 13, 17]

funcs = [m0, m1, m2, m3]


def m0(num):
    return num * 19


def m1(num):
    return num + 6


def m2(num):
    return num ** 2


def m3(num):
    return num + 3


def test(func, nums, mods):
    for num in nums:
        for mod in mods:
            orig = num % mod
            adjust = func(num)
            print((func(orig) % mod) == (adjust % mod))


for func in funcs:
    test(func, nums, mods)
