class Solution:
    def preorderTraversal(self, A):
        stack = [A]
        ans = []

        while stack:
            top = stack.pop()
            ans.append(top.val)

            if top.right:
                ans.append(top.right)

            if top.left:
                stack.append(top.left)

        return ans
