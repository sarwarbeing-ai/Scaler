class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):
        # convert all lowercase to uppercase
        for i in range(len(A)):
            if A[i].isalpha():
                if ord(A[i])>=97:
                   A[i]=chr(ord(A[i])^32)
        return A
