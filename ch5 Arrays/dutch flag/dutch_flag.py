def dutch_flag(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot.
    for i in range(len(A)):
        # Look for a smaller element.
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                print("1st pass: {}".format(A))
                break
    # Second pass: group elements larger than pivot.
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            print("2nd pass break")
            break
        # Look for larger element. Stop when we reach an element less than
        # pivot, since first pass has moved them to the start of A.
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                print("2nd pass: {}".format(A))
                break
    return A



test1 = [0, 1, 2, 0, 2, 1, 1]
test2 = [2, 2, 2, 1, 1, 0, 0]
test3 = [0, 1, 2, 0, 2, 1, 1]


print("test1 results: {}".format(dutch_flag(3, test3)))