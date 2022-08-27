class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # check if A is a balanced string or not
        # A is consists of "(" and ")" only
        res=[]
        if A[0]==")":
            return 0
        for a in A:
            if a=="(":
                res.append(a)
            else:
                if len(res)==0:
                    return 0
                ss=res.pop()
                if ss!="(":
                    return 0
        return (len(res)==0)*1
