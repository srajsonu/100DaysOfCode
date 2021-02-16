class Solution:
    def check(self, root, prev):
        if not root:
            return

        if root.val > prev:
            self.cnt += 1

        l = self.check(root.left, max(prev, root.val))
        r = self.check(root.right, max(prev, root.val))
        return l and r

    def solve(self, A):
        self.cnt = 0
        self.check(A, float('-inf'))
        return self.cnt
