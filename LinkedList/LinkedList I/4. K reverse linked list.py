class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, A, B):
        curr = A
        nxt = None
        prev = None
        cnt = 0

        while curr and cnt < B:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            cnt += 1

        if nxt:
            A.next = self.reverseList(nxt, B)

        return prev
