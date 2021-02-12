class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, A, B):
        l = ListNode(0)
        r = ListNode(0)
        currL = l
        currR = r
        curr = A
        while curr:
            if curr.val <= B:
                l.next = curr
                l = l.next
            else:
                r.next = curr
                r = r.next

            curr = curr.next

        currL = currL.next
        currR = currR.next

        # print(l.val, currL.val, r.val, currR.val)

        tmp = ListNode(0)
        ans = tmp

        while currL and currR:
            if currL.val <= currR.val:
                tmp.next = currL
                currL = currL.next
            else:
                tmp.next = currR
                currR = currR.next

            tmp = tmp.next

        while currL:
            tmp.next = currL
            currL = currL.next
            tmp = tmp.next

        while currR:
            tmp.next = currR
            currR = currR.next
            tmp = tmp.next

        return ans.next
