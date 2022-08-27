class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        import sys
        sys.setrecursionlimit(30000)

        def issubsequence(A,B,m,n):
            if m==0:
                return True
            if n==0:
                return False
            if A[m-1]==B[n-1]:
                return issubsequence(A,B,m-1,n-1)
            return issubsequence(A,B,m,n-1)

        if issubsequence(A,B,len(A),len(B)):
            return "YES"
        return "NO"
