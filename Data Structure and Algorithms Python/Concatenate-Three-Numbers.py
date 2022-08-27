def solve(A, B, C):
    '''
    Given three 2-digit integers, A, B, and C,
    find out the minimum number obtained by concatenating
    them in any order.

    Return the minimum result obtained.
    '''
    mn=min(A,B,C)
    if mn-A==0 and B>=C:
        return int(str(mn)+str(C)+str(B))
    elif mn-A==0 and C>=B:
        return int(str(mn)+str(B)+str(C))

    elif mn-B==0 and A>=C:
        return int(str(mn)+str(C)+str(A))
    elif mn-B==0 and C>=A:
        return int(str(mn)+str(A)+str(C))
    elif mn-C==0 and B>=A:
        return int(str(mn)+str(A)+str(B))
    elif mn-C==0 and A>=B:
        return int(str(mn)+str(B)+str(A))
