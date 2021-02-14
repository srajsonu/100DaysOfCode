class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, A, B):
        if not A or not B:
            return

        node = TreeNode(A.pop(0))
        index = B.index(node.val)
        node.left = self.buildTree(A, B[:index])
        node.right = self.buildTree(A, B[index + 1:])
        return node
