class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        from collections import deque
        qu=deque([1,2,3])
        ans=-1
        result=[]
        for i in range(A):
            ans=qu.popleft()
            result.append(ans)
            for d in [1,2,3]:
                qu.append(ans*10+d)
        return result
