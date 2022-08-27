# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):
        # without using recursion
        result=[]
        stack=[]
        stack.append(A)
        while len(stack)!=0:
            A=stack.pop()
            result.append(A.val)
            if A.right!=None:
                stack.append(A.right)
            if A.left!=None:
                stack.append(A.left)
        return result
