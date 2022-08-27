# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):
        stack=[]
        tstack=[]
        stack.append(A)
        while len(stack)!=0:
            root=stack.pop()
            tstack.append(root)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        result=[]
        while len(tstack)!=0:
            result.append(tstack.pop().val)
        return result
