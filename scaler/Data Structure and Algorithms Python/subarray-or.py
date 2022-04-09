class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self,A):
        mod = 10 ** 9 + 7
        n = len(A)
        ans = 0
        for i in range(27):
            ind = n
            for j in range(n-1, -1,-1):
                bit = bool((A[j] >> i) &1)
                if bit:
                    ind = j
                ans = (ans + ((n-ind)*(2**i)%mod) % mod) % mod
        return ans
