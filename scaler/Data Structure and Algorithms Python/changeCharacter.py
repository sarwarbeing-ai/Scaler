class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # change at most B characters in A to any other lowercase alphabet
        # such that the number of distinct characters in the string is minimized
        S=[]
        for a in "abcdefghijklmnopqrstuvwxyz":
            c=A.count(a)
            S.append(c)
        S.sort()
        for i in range(len(S)):
            if B==0:
                break

            if S[i]<=B:
                B-=S[i]
                S[i]=0
        count_0=S.count(0)
        return len(S)-count_0
        
