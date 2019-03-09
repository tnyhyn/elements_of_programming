# This problem deals with deleting repeated elements in a sorted array. 
# ex: [2, 3, 5, 5, 7, 11, 11, 11, 13] --> [2, 3, 5, 6, 11, 13, 0, 0, 0]
# There is an O(n) time and O(1) space solution


# Naive 
# Time: O(n), Space: O(n)
def del_dup_naive(arr):
    if len(arr) < 2: return arr
    delDup = []
    check = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == check:
            check = arr[i]
            arr[i] = 0
        else: check = arr[i]
    for j in arr:
        if j != 0:
            delDup.append(j)
    return len(delDup)

# Solution
# Time: O(n), Space: O(1)
def del_dup_sol(A):
    if not A:
        return 0
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


## Tests
test1 = [1, 1, 2, 3, 5, 9, 9]
test2 = [2, 3, 5, 5, 7, 11, 11, 11, 13]

def test(tests, func):
    for i in tests:
        print("test:", i, " --> ", func(i))

test([test1, test2], del_dup_naive)
