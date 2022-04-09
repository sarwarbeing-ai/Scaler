class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        d={}
        d[0]=1
        s=0
        for i in range(len(A)):
            s+=A[i]
            if s in d:
                return 1
            d[s]=1
        return 0
