class Solution:
    def inorderTraversal(self, A):
        curr = A
        ans = []
        stack = [A]

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                ans.append(curr.val)
                curr = curr.right

        return ans
