def solve(A):
    '''
    You are given a number A in the form of a string.
    Check if the number is divisible by eight or not.

    Return 1 if it is divisible by eight else, return 0.
    '''
    if len(A)<=2:
        if int(A)%8==0:
            return 1
        return 0
    if int(A[-3:])%8==0:
        return 1
    return 0
