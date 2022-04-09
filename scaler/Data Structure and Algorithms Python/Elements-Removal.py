def solve(A):
    '''
    Given an integer array A of size N. You can remove any element from the array in one operation.
    The cost of this operation is the sum of all elements in the array present before this operation.

    Find the minimum cost to remove all elements from the array.
    '''
    A.sort(reverse=True)
    s=0
    for i in range(len(A)):
        s+=A[i]*(i+1)
    return s
