class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def reverseList(self, A):
        curr = A
        prev = None
        nxt = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        if nxt:
            A.next = self.reverseList(nxt)

        return prev

    def lPalin(self, A):
        slow = A
        fast = A.next

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head1 = A
        head2 = self.reverseList(slow.next)
        while head1 and head2:
            if head1.val != head2.val:
                return 0
            head1 = head1.next
            head2 = head2.next

        return 1
