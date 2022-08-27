class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A==1:
            return 0
        mid=2**(A-1)//2
        if B<=mid:
            return self.solve(A-1,B)
        return 1-self.solve(A-1,B-mid)
