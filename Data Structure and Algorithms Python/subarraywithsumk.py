class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        d={}
        d[0]=-1
        s=0

        for i in range(len(A)):
            s+=A[i]
            if (s-B) in d:

                start=d[s-B]
                end=i+1
                return A[start+1:end]
            else:
                d[s]=i
        return [-1]
