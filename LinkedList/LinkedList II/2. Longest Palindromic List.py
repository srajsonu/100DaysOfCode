class Solution:
    def count_common(self, l, r):
        count = 0
        while l and r:
            if l.val == r.val:
                count += 1
            else:
                break
            l = l.next
            r = r.next

        return count

    def solve(self, A):
        curr = A
        prev = None
        nxt = None

        ans = 1
        while curr:
            nxt = curr.next
            curr.next = prev
            ans = max(ans, 2 * self.count_common(prev, nxt) + 1)
            ans = max(ans, 2 * self.count_common(curr, nxt))
            prev = curr
            curr = nxt

        return ans
