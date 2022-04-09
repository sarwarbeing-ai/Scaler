def solve(A, B):
    '''
    Given two integers A and B,
    find the greatest possible positive integer M,
    such that A % M = B % M.
    '''
    return B-A if B>A else A-B
