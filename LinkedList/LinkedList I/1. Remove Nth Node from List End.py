class Solution:
    def removeNthFromEnd(self, A, B):
        head = A
        size = 0

        while head:
            size += 1
            head = head.next

        node = size - B
        if B >= size:
            return A.next

        head = A
        for _ in range(node - 1):
            head = head.next
        head.next = head.next.next
        return A
