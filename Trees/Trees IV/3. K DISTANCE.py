class Solution:
    def lcs(self, root, B, aux):
        if not root:
            return 0

        l = self.lcs(root.left, B, aux + [root.val])
        r = self.lcs(root.right, B, aux + [root.val])

        cnt = 0
        for i in aux:
            if abs(i - root.val) <= B:
                cnt += 1
        cnt += (l + r)
        return cnt

    def solve(self, A, B):
        return self.lcs(A, B, [])
