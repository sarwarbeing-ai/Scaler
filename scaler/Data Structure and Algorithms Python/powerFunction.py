class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if A==0:
            return 0
        if B==0:
            return 1
        x=pow(A,B//2,C)
        if B%2==0:
            return ((x%C)*(x%C))%C
        return ((A%C)*(x%C)*(x%C))%C
