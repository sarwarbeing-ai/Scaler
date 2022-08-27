class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        if len(A)==1:
            return ""
        d=[]
        for i in range(len(A)):
            d.append((i,A[i]))
        d.sort(key=lambda x:x[1])
        if d[0][0]<d[1][0]:
            return d[0][1]+d[1][1]

        m=d[0]
        for idx,l in d[1:]:
            if m[0]>idx:
                continue
            else:
                return  m[1]+l
        return d[1][1]+m[1]
