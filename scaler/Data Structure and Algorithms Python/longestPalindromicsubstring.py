class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):
		ans=0
		# odd length palindrome
		for i in range(len(A)):
			l=1
			x=i-1
			y=i+1
			while x>=0 and y<len(A):
				if A[x]==A[y]:
					l+=2
					x-=1
					y+=1
				else:
					break
			if ans<l:
				ans=l
				end=y
		# even length palindrome
		for i in range(len(A)-1):
			l=0
			x=i
			y=i+1
			while x>=0 and y<len(A):
				if A[x]==A[y]:
					l+=2
					x-=1
					y+=1
				else:
					break
			if ans<l:
				end=y
				ans=l
		return A[end-ans:end]
