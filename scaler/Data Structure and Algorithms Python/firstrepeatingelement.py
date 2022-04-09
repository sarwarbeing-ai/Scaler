class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        d={}
        for a in A:
            if a in d:
                d[a]+=1
            else:
                d[a]=1
        for k in A:
            if d[k]>1:
                return k
        return -1
