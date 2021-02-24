from heapq import *


class Solution:
    def solve(self, A, B, C, D):
        pq = []
        C.append(A)
        D.append(float('inf'))
        prev = 0
        ans = 0
        for curr, cap, in zip(C, D):
            B -= curr - prev

            while pq and B < 0:
                B += -heappop(pq)
                ans += 1

            if B < 0:
                return -1

            heappush(pq, -cap)
            prev = curr

        return ans


if __name__ == '__main__':
    A = 100
    B = 10
    C = [10, 20, 30, 60]
    D = [60, 30, 30, 40]
    E = Solution()
    print(E.solve(A, B, C, D))
