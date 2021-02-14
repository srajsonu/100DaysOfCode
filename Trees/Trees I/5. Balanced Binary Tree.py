class Solution:
    def check(self, root):
        if not root:
            return 0

        l = self.check(root.left)
        r = self.check(root.right)
        self.ans = max(self.ans, abs(l - r))
        return max(l, r) + 1

    def isBalanced(self, A):
        self.ans = 0
        self.check(A)
        if self.ans > 1:
            return 0
        else:
            return 1
