# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        "find the count of nodes with more value than all its ancestor."
        def recur(A,maximum):
            if A is None:
                return 0
            count=0
            if A.val>maximum:
                maximum=A.val
                count=1
            return count+recur(A.left,maximum)+recur(A.right,maximum)

        return recur(A,float("-inf"))



        
