import itertools
import operator


data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]

## itertools.accumulate
list(itertools.accumulate(data, operator.mul))
    # [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
list(itertools.accumulate(data, max))
    # [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]


## itertools.combinations
list(itertools.combinations('ABCD', 2))
# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]


## itertools.count
    # list(itertools.count(0, 1)) ---> 0 1 2 3 4...


## itertools.cycle
    # itertools.cycle('ABCD') ---> ABCDABCDABCDABCD...


## itertools.groupby
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D


## itertools.isslice
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G


## itertools.product
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111


## itertools.repeat
    # repeat(10, 3) --> 10 10 10
    # list(map(pow, range(10), repeat(2)))
    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    