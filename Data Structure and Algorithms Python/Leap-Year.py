def solve(A):
    '''
    Given an integer A representing a year, Return 1 if it is a
    leap year else, return 0.
    '''
    if A%100==0 and A%4!=0:
        return 0
    elif A%100==0 and (A//100)%4==0:
        return 1
    elif A%4==0 and A%100!=0:
        return 1
    else:
        return 0
