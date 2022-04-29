class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        # passing game is going on ,initially B posses the ball
        # C is list of ID and 0
        # B will pass forward to the player with id=ID
        # if id=0 then the player who has the ball in possession will
        # pass back to the player who had forwarded the ball to him
        # return ID after A passes
        res=[]
        res.append(B)
        i=0
        for _ in range(A):
            if C[i]==0:
                res.pop()
                i+=1
            else:
                res.append(C[i])
                i+=1
        return A if len(res)==0 else res.pop()
