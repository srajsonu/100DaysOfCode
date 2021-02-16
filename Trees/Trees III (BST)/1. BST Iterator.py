class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.ans = []
        self.cnt = 0
        self.insert(root)

    def insert(self, root):
        if not root:
            return

        self.insert(root.left)
        self.ans.append(root.val)
        self.insert(root.right)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        n = len(self.ans)
        if self.cnt == n:
            return 0
        else:
            return 1

    # @return an integer, the next smallest number
    def next(self):
        ans = self.ans[self.cnt]
        self.cnt += 1
        return ans
