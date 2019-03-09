def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i -1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

def test(A, name):
    print(name, ":", A, end=" ")
    A = plus_one(A)
    print("incremented to {}".format(A))

t1 = [1,2,3,4,5,6]
t2 = [9,9,9,9]
t3 = [0]
t4 = [1,2,9,9]
t5 = [9]

test(t1, "t1")
test(t2, "t2")
test(t3, "t3")
test(t4, "t4")
test(t5, "t5")