class Solution:
    def leftView(self, root, level):
        if not root:
            return
        if level not in self.ans:
            self.ans[level] = root.val
        self.leftView(root.left, level + 1)
        self.leftView(root.right, level + 1)

    def solve(self, A):
        self.ans = {}
        self.leftView(A, 0)
        return [i for i in self.ans.values()]
