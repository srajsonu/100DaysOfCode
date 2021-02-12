class Solution:
    def merge(self, l, r):
        if not l:
            return r

        if not r:
            return l

        ans = None
        if l.val <= r.val:
            ans = l
            ans.down = self.merge(l.down, r)
        else:
            ans = r
            ans.down = self.merge(l, r.down)

        ans.right = None
        return ans

    def flatten(self, root):
        if not root or not root.right:
            return root

        right = self.flatten(root.right)
        ans = self.merge(root, right)
        return ans
