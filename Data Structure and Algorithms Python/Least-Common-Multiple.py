def LCM(A, B):
    '''
    Find least common multiple of A and B (integers)
    '''
    S1=A
    S2=B
    while B!=0:
        A,B=B,A%B
    return int(S1*S2/A) 
