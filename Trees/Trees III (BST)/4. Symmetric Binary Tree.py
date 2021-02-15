class Solution:
    def check(self, root1, root2):
        if not root1 and not root2:
            return 1

        if not root1 or not root2:
            return 0

        l = self.check(root1.left, root2.right)
        r = self.check(root1.right, root2.left)
        return l and r

    def isSymmetric(self, A):
        return self.check(A, A)
