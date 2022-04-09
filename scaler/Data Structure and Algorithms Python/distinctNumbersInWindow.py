class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
        if B>len(A):
            return []
        res=[]
        d={}
        for i in range(B):
            if A[i] not in d:
                d[A[i]]=1
            else:
                d[A[i]]+=1
        res.append(len(d))
        for i in range(len(A)-B):
            j=i+B-1
            # new element
            if A[j+1] not in d:
                d[A[j+1]]=1
            else:
                d[A[j+1]]+=1
            # old element
            d[A[i]]-=1
            if d[A[i]]==0:
                del d[A[i]]
            res.append(len(d))
        return res
