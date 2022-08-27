class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        d = {}
        i = 1
        for lttrs in B:
            d[lttrs] = i
            i += 1
        i = 0
        j = 0
        x = 0
        while i < len(A):
            if d[A[i][x]] < j:
                return 0
            elif d[A[i][x]] > j:
                j = d[A[i][x]]
            else:
                while x < len(A[i-1]):
                    j = d[A[i-1][x]]
                    if x >= len(A[i]):
                        return 0
                    elif d[A[i][x]] > j:
                        break
                    x += 1
            x = 0
            j = d[A[i][x]]
            i += 1
        return 1
