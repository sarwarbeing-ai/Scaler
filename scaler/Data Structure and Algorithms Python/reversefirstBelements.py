class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        # reverse first B elements of the list A using queue
        from collections import deque
        qu=deque(A)
        if B==1:
            return qu
        res=[]
        for i in range(B):
            res.append(qu.popleft())
        for elt in res:
            qu.appendleft(elt)
        return qu
