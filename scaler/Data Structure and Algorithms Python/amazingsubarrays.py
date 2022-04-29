class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # find all amazing substrings of A
        # an amazing is one that starts with a vowel
        num=0
        n=len(A)
        for i in range(n):
            if A[i] in 'aeiouAEIOU':
                num+=1
                num+=n-i-1
        return num%10003
