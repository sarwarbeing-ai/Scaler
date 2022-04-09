class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def subsets(self, A):
        A.sort()
        res=[]
        for i in range(2**len(A)):
            l=[]
            for j in range(len(A)):
                if i&(1<<j)!=0:
                    l.append(A[j])
            res.append(l)
        res.sort()
        return res
