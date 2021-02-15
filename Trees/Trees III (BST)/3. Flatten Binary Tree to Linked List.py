class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        if not root:
            return

        l = self.flatten(root.left)
        r = self.flatten(root.right)

        root.left = None
        root.right = l
        tmp = root

        while tmp.right:
            tmp = tmp.right

        tmp.right = r
        return root
