def solve(A):
    '''
    Given an integer array A of size N. Return 1 if the array
    can be arranged to form an arithmetic progression, otherwise
    return 0.
    '''
    A.sort()
    d=A[1]-A[0]
    for i  in range(len(A)-1):
        if (A[i+1]-A[i])!=d:
            return 0
    return 1
