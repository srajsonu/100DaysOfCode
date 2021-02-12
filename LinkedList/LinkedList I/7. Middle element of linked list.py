class Solution:
    def solve(self, A):
        slow = A
        fast = A

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.val
