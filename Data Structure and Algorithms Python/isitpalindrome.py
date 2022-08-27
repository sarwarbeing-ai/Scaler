class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # check if A is palindrome or not
        n=len(A)
        i=0
        j=n-1
        while i<j:
            if A[i]!=A[j]:
                return 0
            i+=1
            j-=1
        return 1
