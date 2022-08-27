class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        def recur(A,B,i):
            if i==len(A):
                if B==0:
                    return True
                return False
            if recur(A,B-A[i],i+1) or recur(A,B,i+1):
                return True
            return False
        if recur(A,B,0):
            return 1
        return 0
