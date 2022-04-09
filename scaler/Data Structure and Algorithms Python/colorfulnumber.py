class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):
        A=str(A)
        d={}
        for i in range(len(A)):
            if int(A[i]) not in d:
                d[int(A[i])]=1
            else:
                return 0
            ans=int(A[i])
            for j in range(i+1,len(A)):
                ans*=int(A[j])
                if ans not in d:
                    d[ans]=1
                else:
                    return 0
        return 1
