# assuming list are of the same length
# not using iteration either

def combine_lists(A, B):
    length = len(A)

    ret = list()
    for i in range(length):
        ret.append(A[i])
        ret.append(B[i])

    return ret


A = ['a', 'b', 'c']
B = [1, 2, 3]

print(combine_lists(A, B))