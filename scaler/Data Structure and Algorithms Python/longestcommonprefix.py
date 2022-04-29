class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
        if len(A)==1:
            return A[0]
        mx_string=min(A,key=lambda x:len(x))
        prefix=''

        for i in range(len(mx_string)):
            b=mx_string[i]
            for j in range(len(A)):
                if A[j][i]!=b:
                    return prefix
            prefix+=b
        return prefix
