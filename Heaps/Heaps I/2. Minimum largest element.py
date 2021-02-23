from heapq import *


class Solution:
    def solve(self, A, B):
        n = len(A)
        pq = []
        C = [i for i in A]

        for i in range(n):
            heappush(pq, (C[i] * 2, i))

        while B:
            tmp, idx = heappop(pq)
            C[idx] += A[idx]
            heappush(pq, (tmp + A[idx], idx))
            B -= 1

        return max(C)




if __name__ == '__main__':
    A = [5, 1, 4, 2]
    B = 5
    C = Solution()
    print(C.solve(A, B))
