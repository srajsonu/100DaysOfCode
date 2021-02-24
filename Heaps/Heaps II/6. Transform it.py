from heapq import *


class Solution:
    def solve(self, A, B):
        n = len(A)
        mn = []
        nxt = [i for i in A]

        for i in range(n):
            heappush(mn, (A[i]*2, i))

        while B:
            tmp, i = heappop(mn)
            nxt[i] += A[i]
            heappush(mn, (tmp + A[i], i))
            B -= 1

        return max(nxt)


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    B = 3
    C = Solution()
    print(C.solve(A, B))
