def titleToNumber(A):
    '''
    Given a column title as appears in an Excel sheet,
    return its corresponding column number.
    '''
    result=0
    for i in range(len(A)):
        result*=26
        result+=ord(A[i])-ord('A')+1
    return result
