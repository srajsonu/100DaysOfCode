class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    def buildTree(self, A, B):
        if not A or not B:
            return

        node = TreeNode(B.pop())
        index = A.index(node.val)
        node.right = self.buildTree(A[index+1:], B)
        node.left = self.buildTree(A[:index], B)
        return node
