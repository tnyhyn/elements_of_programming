def dutch_flag(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
            print("1st pass: {}, smaller: {}".format(A, smaller))
    # Second pass: group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
            print("2nd pass: {}, larger: {}".format(A, larger))
    return A


test1 = [0, 1, 2, 0, 2, 1, 1]
test2 = [2, 2, 2, 1, 1, 0, 0]
test3 = [0, 1, 2, 0, 2, 1, 1]


print("test1 results: {}".format(dutch_flag(3, test3)))