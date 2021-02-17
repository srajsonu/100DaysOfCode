class ListNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class custom:
    def __init__(self):
        self.val = None
        self.inc = 1
        self.dec = 1


class Solution:
    def dfs(self, root, parent):
        if not root:
            return custom()

        l = self.dfs(root.left, root.val)
        r = self.dfs(root.right, root.val)

        curr = custom()

        if l.val and r.val:
            if l.val + 1 == root.val and r.val - 1 == root.val:
                curr.inc = l.inc + r.inc
                curr.dec = l.dec + r.dec

            elif l.val + 1 == root.val:
                curr.dec = l.dec + 1

            elif l.val - 1 == root.val:
                curr.inc = l.inc + 1

            elif r.val + 1 == root.val:
                curr.dec = r.dec + 1

            elif r.val - 1 == root.val:
                curr.inc += 1

            curr.val = root.val

        if parent - root.val == 1:
            curr.val = root.val
            curr.dec += 1

        if root.val - parent == 1:
            curr.val = root.val
            curr.inc += 1

        self.ans = max(self.ans, curr.inc + curr.dec - 1)
        return curr

    def solve(self, root):
        self.ans = 0
        self.dfs(root, 0)
        return self.ans


if __name__ == '__main__':
    root = ListNode(1)
    root.right = ListNode(3)
    root.right.left = ListNode(2)
    root.right.left.left = ListNode(1)
    root.right.right = ListNode(4)
    root.right.right.right = ListNode(5)

    A = Solution()
    print(A.solve(root))
