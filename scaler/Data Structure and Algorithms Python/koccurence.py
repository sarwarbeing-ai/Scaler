class Solution:
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def getSum(self, B, C):
        # sum of all the elements in C which apears B times
        d={}
        for a in C:
            if a in d:
                d[a]+=1
            else:
                d[a]=1
        s=0
        flag=False
        for k in d:
            if d[k]==B:
                flag=True
                s+=k
        if flag:
            return s%(10**9+7)
        return -1
