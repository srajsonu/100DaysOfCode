from _heapq import *


class Solution:
    def build_heap(self, x, mx, mn):
        if len(mx) == len(mn):
            heappush(mx, -x)
            heappush(mn, -heappop(mx))
        else:
            heappush(mn, x)
            heappush(mx, -heappop(mn))

    def find_median(self, mx, mn):
        if len(mx) > len(mn):
            tmp = heappop(mx)
            heappush(mx, tmp)
            return -tmp
        elif len(mx) < len(mn):
            tmp = heappop(mn)
            heappush(mn, tmp)
            return tmp
        else:
            x = -heappop(mx)
            y = heappop(mn)
            med = (x + y) / 2
            heappush(mx, -x)
            heappush(mn, y)
            return med

    def check(self, A, mx, mn):
        n = len(A)
        for i in range(1, n):
            self.build_heap(A[i-1], mx, mn)
            if self.find_median(mx, mn) == A[i]:
                return 1

        return 0


    def solve(self, A):
        mx = []
        mn = []
        l = self.check(A, mx, mn)
        mx.clear()
        mn.clear()

        A.reverse()
        r = self.check(A, mx, mn)
        if l or r:
            return 1
        return 0

if __name__ == '__main__':
    A = [4, 6, 8, 4]
    B = Solution()
    print(B.solve(A))
