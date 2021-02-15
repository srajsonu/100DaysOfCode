class Solution:
    def rightView(self, root, level):
        if not root:
            return

        if level not in self.ans:
            self.ans[level] = root.val

        self.rightView(root.right, level + 1)
        self.rightView(root.left, level + 1)

    def solve(self, A):
        self.ans = {}
        self.rightView(A, 0)
        return [i for i in self.ans.values()]
