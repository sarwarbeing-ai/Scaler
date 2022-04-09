class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        import sys
        sys.setrecursionlimit(30000)
        s=0
        e=len(A)-1
        return 1*(self.ispalindrome(A,s,e))

    def ispalindrome(self,A,s,e):
        if s>=e:
            return True
        if A[s]==A[e] and self.ispalindrome(A,s+1,e-1):
            return True
        return False
