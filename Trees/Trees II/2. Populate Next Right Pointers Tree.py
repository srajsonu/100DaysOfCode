class Solution:
    def getNextRight(self, nxt):
        nxt = nxt.next

        while nxt:
            if nxt.left:
                return nxt.left

            if nxt.right:
                return nxt.right

            nxt = nxt.next

        return nxt

    def connect(self, root):
        if not root:
            return

        curr = root
        while curr:
            nxt = curr
            while nxt:
                if nxt.left:
                    if nxt.right:
                        nxt.left.next = nxt.right
                    else:
                        nxt.left.next = self.getNextRight(nxt)

                if nxt.right:
                    nxt.right.next = self.getNextRight(nxt)

                nxt = nxt.next

            if curr.left:
                curr = curr.left
            elif curr.right:
                curr = curr.right
            else:
                curr = self.getNextRight(curr)


