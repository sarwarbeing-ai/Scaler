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
        c=0
        stack=[]
        while A!=None or len(stack)!=0:
            if A!=None:
                stack.append(A)
                A=A.left
            else:
                A=stack.pop()
                c+=1
                A=A.right
        return c
