class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
        ans=-len(A)
		S=set(A)
        for i in range(len(A)):
			if A[i]-1 in S:
				continue
			else:
				cnt=0
				val=A[i]
				while  val in S:
					val+=1
					cnt+=1
				ans=max(ans,cnt)
		return ans
