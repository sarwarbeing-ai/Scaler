class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        mx=0
        A.sort()
        for i in range(len(A)):
            mx+=(2**i)*A[i]
        mn=0
        for i in range(len(A)):
            mn+=(2**(len(A)-(i+1)))*A[i]
        return int((mx-mn)%(1000000007))
