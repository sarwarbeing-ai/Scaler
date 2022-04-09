class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        d={}
        d[A[0]]=[0]
        for i in range(1,len(A)):
            if A[i] in d:
                d[A[i]].append(i)
            else:
                d[A[i]]=[i]
        mn=len(A)
        for k in d:
            if len(d[k])>1:
                mn=min(abs(d[k][0]-d[k][1]),mn)
        if mn==len(A):
            return -1
        return mn
