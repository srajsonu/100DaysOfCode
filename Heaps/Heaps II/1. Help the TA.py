from heapq import *


class Solution:
    def solve(self, A, B):
        n = len(A)
        pq = []
        for i in range(n):
            heappush(pq, (-A[i], i))

        ans = []
        while B:
            tmp, idx = heappop(pq)
            if tmp == 0:
                break
            ans.append(idx)
            heappush(pq, (tmp+1, idx))
            B -= 1

        return ans

if __name__ == '__main__':
    A = [4, 2, 5, 3, 6]
    B = 4
    C = Solution()
    print(C.solve(A, B))
