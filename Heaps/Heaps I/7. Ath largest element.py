from heapq import *


class Solution:
    def solve(self, A, B):
        n = len(B)
        pq = []
        ans = []
        cnt = 0
        for i in range(n):
            heappush(pq, B[i])
            cnt += 1
            if cnt < A:
                ans.append(-1)

            elif cnt == A:
                tmp = heappop(pq)
                ans.append(tmp)
                heappush(pq, tmp)
            else:
                heappop(pq)
                cnt -= 1
                if cnt == A:
                    tmp = heappop(pq)
                    ans.append(tmp)
                    heappush(pq, tmp)


        return ans

if __name__ == '__main__':
    A = 4
    B = [1, 2, 3, 4, 5, 6]
    C = Solution()
    print(C.solve(A, B))
