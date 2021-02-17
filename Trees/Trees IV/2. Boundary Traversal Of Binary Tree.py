class Solution:
    def left(self, root, aux):
        if root:
            if root.left:
                aux.append(root.val)
                self.left(root.left, aux)
            elif root.right:
                aux.append(root.val)
                self.left(root.right, aux)

        return aux

    def right(self, root, aux):
        if root:
            if root.right:
                aux.append(root.val)
                self.right(root.right, aux)
            elif root.left:
                aux.append(root.val)
                self.right(root.left, aux)

        return aux

    def leaf(self, root, aux):
        if root:
            self.leaf(root.left, aux)

            if not root.left and not root.right:
                aux.append(root.val)

            self.leaf(root.right, aux)

        return aux

    def solve(self, root):
        ans = []
        if root:
            ans.append(root.val)
            self.left(root.left, ans)
            self.leaf(root, ans)
            self.right(root.right, ans)

        return ans

if __name__ == '__main__':
    pass
