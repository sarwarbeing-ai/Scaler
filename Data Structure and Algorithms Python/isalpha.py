class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        # check if all characters in A is alphabet
        for a in A:
            if ord(a)<65:
                return 0
            if ord(a)>90 and ord(a)<97:
                return 0

            if ord(a)>122:
                return 0
        return 1
