class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
        d={}
        for i in range(len(A)):
            if B+A[i] in d or A[i]-B in d:
                return 1
            else:
                if A[i] not in d:
                    d[A[i]]=1
        return 0
