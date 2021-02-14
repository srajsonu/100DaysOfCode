from collections import deque, defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root, level):
        if not root:
            return

        if level % 2 == 0:
            self.ans[level].append(root.val)
        else:
            self.ans[level].appendleft(root.val)

        self.levelOrder(root.left, level+1)
        self.levelOrder(root.right, level+1)

    def zigzagLevelOrder(self, A):
        self.ans = defaultdict(deque)
        self.levelOrder(A, 0)
        return [i for i in self.ans.values()]
