def solve(A):
    '''Given an integer array A, find if an integer p exists
       in the array such that the number of integers greater than p
       in the array equals p.
    '''
    A.sort(reverse=True)
    res=[0]*len(A)
    for i in range(1,len(A)):
        if A[i]==A[i-1]:
            res[i]=res[i-1]
        else:
            res[i]=i
    for i in range(len(A)):
        if res[i]==A[i]:
            return 1
    return -1
