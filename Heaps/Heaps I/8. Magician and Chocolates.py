from heapq import *


class Solution:
    def nchoc(self, A, B):
        mod = 10 ** 9 + 7
        n = len(B)
        pq = []

        for i in range(n):
            heappush(pq, -B[i])

        ans = 0
        while A:
            tmp = -heappop(pq)
            ans += tmp
            ans %= mod
            heappush(pq, -(tmp//2))
            A -= 1

        return ans


if __name__ == '__main__':
    A = 5
    B = [2, 4, 6, 8, 10]
    C = Solution()
    print(C.nchoc(A, B))
