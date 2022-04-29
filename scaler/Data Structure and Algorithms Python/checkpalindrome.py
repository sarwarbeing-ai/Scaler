class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # check if A can be rearranged to form palindrome
        d={}
        for a in A:
            if a in d:
                d[a]+=1
            else:
                d[a]=1
        if len(A)%2==0:
            for k in d:
                if d[k]%2!=0:
                    return 0
            return 1
        else:
            c_even=0
            c_odd=0
            for k in d:
                if d[k]%2==0:
                    c_even+=1
                else:
                    c_odd+=1
            if c_odd>1:
                return 0

            return 1
