# Write a function that encodes a string into an integer without using int()
# and a function that converts an int to string without using str()
# ex: "123" returns 123
# It should also handle negatives

import functools
import string


# Naive | string to int


# Solution
def itos(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    s = []
    while True:
        s.append(chr(ord('0') + x%10))
        x //= 10
        if x == 0:
            break
    return ('-' if is_negative else '') + ''.join(reversed(s))

def stoi(s):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c), 
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


# Tests
test1 = 12345
test2 = 2707

test3 = "12345"
test4 = "2707"

def itos_test(tests, func):
    for i in tests:
        print("test: ", i, " --> ", func(i))

itos_test([test1, test2], itos)
itos_test([test3, test4], stoi)
