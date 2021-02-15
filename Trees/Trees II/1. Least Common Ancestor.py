class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = []

    def find(self, A, B, C, ans):
        if not A:
            return

        if A.val == B or A.val == C:
            self.ans.append(ans + [A.val])
            return

        l = self.find(A.left, B, C, ans + [A.val])
        r = self.find(A.right, B, C, ans + [A.val])
        return l or r

    def lca(self, root, B, C):
        if not root:
            return

        if root.val == B or root.val == C:
            return root

        l = self.lca(root.left, B, C)
        r = self.lca(root.right, B, C)

        if l and r:
            return root

        return l if l else r


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # root.left.left.right = TreeNode(2)
    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)
    # root.right.right.right = TreeNode(1)
    B = 4
    C = 5
    D = Solution()
    print(D.lca(root, B, C))
