class Solution:
    def postOrder(self, A):
        curr = A
        ans = []
        s1 = []
        s2 = []
        s1.append(curr)

        while s1:
            top = s1.pop()
            s2.append(top)
            if top.left:
                s1.append(top.left)
            if top.right:
                s1.append(top.right)

        while s2:
            top = s2.pop()
            ans.append(top.val)

        return ans

    def postorderTraversal(self, A):
        stack = [A]
        ans = []

        while stack:
            top = stack.pop()
            ans.append(top.val)

            if top.left:
                stack.append(top.left)

            if top.right:
                stack.append(top.right)

        return ans[::-1]
