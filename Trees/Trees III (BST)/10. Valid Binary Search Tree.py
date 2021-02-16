class BST:
    def __init__(self):
        self.isBST = 1
        self.min = float('inf')
        self.max = float('-inf')

class Solution:
    def check(self, root):
        curr = BST()
        if not root:
            return curr

        l = self.check(root.left)
        r = self.check(root.right)

        curr.min = min(root.val, l.min)
        curr.max = max(root.val, r.max)

        if l.isBST and r.isBST and l.max < root.val and r.min > root.val:
            curr.isBST = 1
        else:
            curr.isBST = 0

        return curr

    def checkBST(self, root, mn, mx):
        if not root:
            return 1

        if root.val <= mn or root.val >= mx:
            return 0

        l = self.checkBST(root.left, mn, root.val)
        r = self.checkBST(root.right, root.val, mx)
        return l and r


    def isValidBST(self, A):
        ans = self.check(A)
        return ans.isBST, self.checkBST(A, float('-inf'), float('inf'))

if __name__ == '__main__':
    pass
