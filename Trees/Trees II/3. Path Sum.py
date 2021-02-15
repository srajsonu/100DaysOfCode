class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, A, B):
        if not A:
            return 0

        if (B - A.val) == 0 and not A.left and not A.right:
            return 1

        l = self.hasPathSum(A.left, B - A.val)
        r = self.hasPathSum(A.right, B - A.val)
        return l or r


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    B = 22
    C = Solution()
    print(C.hasPathSum(root, B))
