class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, A, B):
        currA = A
        currB = B
        sm = 0
        carry = 0
        dummy = ListNode(0)
        ans = dummy

        while currA and currB:
            sm = currA.val + currB.val + carry
            carry = sm // 10
            if sm > 9:
                sm = sm % 10
            dummy.next = ListNode(sm)
            dummy = dummy.next
            currA = currA.next
            currB = currB.next

        while currA:
            sm = currA.val + carry
            carry = sm // 10
            if sm > 9:
                sm = sm % 10
            dummy.next = ListNode(sm)
            dummy = dummy.next
            currA = currA.next

        while currB:
            sm = currB.val + carry
            carry = sm // 10
            if sm > 9:
                sm = sm % 10
            dummy.next = ListNode(sm)
            dummy = dummy.next
            currB = currB.next

        if carry:
            dummy.next = ListNode(carry)

        return ans.next
