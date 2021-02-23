from heapq import *


class Solution:
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        A.sort(reverse=True)
        B.sort(reverse=True)

        pq = []
        heappush(pq, (-(A[0] + B[0]), (0, 0)))
        index = set()
        index.add((0, 0))

        ans = []
        while n:
            j, (k, l) = heappop(pq)
            ans.append(-j)
            
            idx = -1
            sm = -1
            if k < m-1:
                sm = A[k+1] + B[l]
                idx = (k+1, l)
                if idx not in index:
                    heappush(pq, (-sm, idx))
                    index.add(idx)

            if l < m-1:
                sm = A[k] + B[l+1]
                idx = (k, l+1)
                if idx not in index:
                    heappush(pq, (-sm, idx))
                    index.add(idx)

            n -= 1

        return ans





if __name__ == '__main__':
    A = [1, 4, 2, 3]
    B = [2, 5, 1, 6]
    C = Solution()
    print(C.solve(A, B))
