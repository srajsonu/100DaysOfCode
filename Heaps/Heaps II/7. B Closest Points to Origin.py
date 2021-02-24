from heapq import *
from math import sqrt


class Solution:
    def solve(self, A, B):
        ans = []
        pq = []
        for i ,j in A:
            dis = sqrt(i ** 2 + j ** 2)
            heappush(pq, (dis, i, j))

        for _ in range(B):
            dis, i, j = heappop(pq)
            ans.append([i, j])

        return ans



if __name__ == '__main__':
    A = [[1, 3],
         [-2, 2]]
    B = 1
    C = Solution()
    print(C.solve(A, B))
