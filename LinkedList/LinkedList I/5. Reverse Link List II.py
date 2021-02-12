class Solution:
    def reverseBetween(self, A, B, C):
        curr = A
        tmp = None
        prev = None
        nxt = None
        cnt = 0

        while curr and cnt < B - 1:
            tmp = curr
            curr = curr.next
            cnt += 1

        tmp2 = curr

        while curr and cnt < C:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            cnt += 1

        if tmp:
            tmp.next = prev
        else:
            A = prev

        if tmp2:
            tmp2.next = nxt

        return A
