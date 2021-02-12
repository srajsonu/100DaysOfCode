class Solution:
    def detectCycle(self, A):
        slow = A
        fast = A
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None
