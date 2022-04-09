class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count=0
        d={}
        for i in range(len(A)):
            if B^A[i] in d:
                count+=1
            else:
                d[A[i]]=1
        return count
