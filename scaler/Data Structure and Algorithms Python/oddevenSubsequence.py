class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l=1
        idx=1-A[0]%2
        for i in range(len(A)):
            if A[i]%2==idx:
                l+=1
                idx=1-A[i]%2
        return l
