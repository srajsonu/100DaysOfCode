class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, A, B, ans):
        if not A:
            return 0

        if (B - A.val) == 0 and not A.left and not A.right:
            self.ans.append(ans + [A.val])
            return 1

        l = self.hasPathSum(A.left, B - A.val, ans + [A.val])
        r = self.hasPathSum(A.right, B - A.val, ans + [A.val])
        return l or r

    def pathSum(self, A, B):
        self.ans = []
        self.hasPathSum(A, B, [])
        return self.ans


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    B = 22
    C = Solution()
    print(C.pathSum(root, B))
