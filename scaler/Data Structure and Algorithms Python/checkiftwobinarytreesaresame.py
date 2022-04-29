# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):
        res_A=[]
        s_A=[]
        res_B=[]
        s_B=[]
        while A!=None or len(s_A)!=0:
            if A!=None:
                s_A.append(A)
                A=A.left
            else:
                A=s_A.pop()
                res_A.append(A.val)
                A=A.right
        while B!=None or len(s_B)!=0:
            if B!=None:
                s_B.append(B)
                B=B.left
            else:
                B=s_B.pop()
                res_B.append(B.val)
                B=B.right
        if len(res_A)!=len(res_B):
            return 0
        for i in range(len(res_A)):
            if res_A[i]!=res_B[i]:
                return 0
        return 1
