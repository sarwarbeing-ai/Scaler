class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        result=[]
        def recur(A):
            if A==0:
                return result.append(0)

            recur(A-1)
            n=len(result)
            mask=(1<<(A-1))
            for i in range(n-1,-1,-1):
                result.append(result[i]|mask)

        recur(A)
        return result
