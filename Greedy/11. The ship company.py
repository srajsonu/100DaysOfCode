from heapq import *


class Solution:
    def solve(self, A, B, C):
        mx = []
        mn = []

        for i in range(B):
            heappush(mx, -C[i])
            heappush(mn, C[i])

        cost1 = 0
        person = A
        while person:
            tmp = -heappop(mx)
            if tmp == 0:
                continue
            cost1 += tmp
            heappush(mx, -tmp + 1)
            person -= 1

        cost2 = 0
        while A:
            tmp = heappop(mn)
            if tmp == 0:
                continue
            cost2 += tmp
            heappush(mn, tmp-1)
            A -= 1

        return [cost1, cost2]


if __name__ == '__main__':
    A = 4
    B = 3
    C = [2, 1, 1]
    D = Solution()
    print(D.solve(A, B, C))
