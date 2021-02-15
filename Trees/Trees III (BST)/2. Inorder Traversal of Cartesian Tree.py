class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left =  None
        self.right = None

class Solution:
    def build(self, A, l, h):
        if l > h:
            return

        val = max(A[l:h + 1])
        idx = A.index(val)
        root = TreeNode(val)
        root.left = self.build(A, l, idx - 1)
        root.right = self.build(A, idx + 1, h)
        return root

    def buildTree(self, A):
        return self.build(A, 0, len(A) - 1)
