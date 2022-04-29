class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        # toggle each each letter of A
        A=list(A)
        n=len(A)
        for i in range(n):
            A[i]=chr(ord(A[i])^32)
        return "".join(A)
