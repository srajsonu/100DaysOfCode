class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


class Solution:
    def solve(self, A):
        curr = A

        # Copy of every node one after another
        while curr:
            new = ListNode(curr.val)
            new.next = curr.next
            curr.next = new
            curr = curr.next.next

        curr = A
        # Copy value of random nodes
        while curr:
            curr.next.random = curr.random.next
            curr = curr.next.next

        curr = A
        dup_node = A.next

        while curr.next:
            tmp = curr.next
            curr.next = curr.next.next
            curr = tmp

        return dup_node
