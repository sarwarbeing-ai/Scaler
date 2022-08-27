class Solution:
	# @param A : list of integers
	# @return a list of integers
	def lszero(self, A):
        s=0
        max_len=0
        d={}
        for i in range(len(A)):
            if A[i]==0 and max_len==0:
                max_len=1
                end=i+1
            s+=A[i]
            if s==0:
                max_len=i+1
                end=i+1
            if s in d:
                if max_len<(i-d[s]):
                    max_len=i-d[s]
                    end=i+1
            else:
                d[s]=i
        if max_len==0:
            return []
        return A[end-max_len:end]
