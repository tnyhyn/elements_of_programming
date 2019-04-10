import itertools


data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]

def gen(n):
    for i in range(0,n):
        yield i

g = gen(5)

print(g)