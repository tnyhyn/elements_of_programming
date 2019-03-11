ex1 = [x ** 2 for x in range(6)]
ex2 = [x ** 2 for x in range(6) if x%2 == 0]

A = [1, 3, 5]
B = ['a', 'b']

ex3 = [(x, y) for x in A for y in B]

print("example 1: {0}".format(ex1))
print("example 2: {0}".format(ex2))
print("example 3: {0}".format(ex3))