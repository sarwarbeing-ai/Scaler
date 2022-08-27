class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        d1={}
        d2={}
        for a in A:
            if a in d1:
                d1[a]+=1
            else:
                d1[a]=1
        for b in B:
            if b in d2:
                d2[b]+=1
            else:
                d2[b]=1
        C=[]
        for k in d1:
            try:
                c1=d1[k]
                c2=d2[k]
                C+=[k]*min(c1,c2)
            except:
                pass
        return C
