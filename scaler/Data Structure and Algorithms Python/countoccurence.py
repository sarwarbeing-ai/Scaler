class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # find currence of bob in A
        i=0
        count=0
        while i<(len(A)-2):
            if A[i:i+3]=="bob":
                count+=1
                i+=2
            else:
                i+=1
        return count
