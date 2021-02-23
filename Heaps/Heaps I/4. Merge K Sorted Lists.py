from heapq import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, A):
        n = len(A)
        pq = []

        for i in range(n):
            heappush(pq, (A[i].val, A[i]))

        dummy = ListNode(0)
        ans = dummy

        while pq:
            i, j = heappop(pq)
            dummy.next = ListNode(i)
            if j.next:
                heappush(pq, (j.next.val, j.next))
            dummy = dummy.next

        return ans.next

    def solve(self, A):
        ans = self.mergeKLists(A)
        while ans:
            print(ans.val)
            ans = ans.next




if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(10)
    root.next.next = ListNode(20)

    root1 = ListNode(4)
    root1.next = ListNode(11)
    root1.next.next = ListNode(13)

    root2 = ListNode(3)
    root2.next = ListNode(8)
    root2.next.next = ListNode(9)

    A = [root, root1, root2]
    B = Solution()
    print(B.solve(A))
