class Solution:
    def dp(self, root):
        if not root:
            return 0

        l = self.dp(root.left)
        r = self.dp(root.right)

        c1 = l + root.val
        c2 = root.val + r
        c3 = l + root.val + r
        c4 = root.val

        self.ans = max(self.ans, c1, c2, c3, c4)
        return max(l,r, 0) + root.val

    def maxPathSum(self, root):
        self.ans = float('-inf')
        self.dp(root)
        return self.ans
