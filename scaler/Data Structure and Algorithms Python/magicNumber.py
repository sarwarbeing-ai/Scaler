class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A==1:
            return 1
        while True:
            A=self.helper(A)
            if A==1:
                return A
            if A<=9 and A>=2:
                return 0


    def helper(self,x):
        if x==0:
            return 0
        return x%10+self.helper(x//10)
