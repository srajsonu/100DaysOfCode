class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def mergeTwoLists(self, A, B):
        root1 = A
        root2 = B
        curr = ListNode(0)
        ans = curr
        while root1 and root2:
            if root1.val <= root2.val:
                curr.next = root1
                root1 = root1.next
            else:
                curr.next = root2
                root2 = root2.next

            curr = curr.next

        while root1:
            curr.next = root1
            root1 = root1.next
            curr = curr.next

        while root2:
            curr.next = root2
            root2 = root2.next
            curr = curr.next

        return ans.next
