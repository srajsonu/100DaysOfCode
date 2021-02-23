from heapq import *


class Solution:
    def find_median(self, mx, mn, ans):
        if len(mx) >= len(mn):
            tmp = heappop(mx)
            ans.append(-tmp)
            heappush(mx, tmp)
        else:
            tmp = heappop(mn)
            ans.append(tmp)
            heappush(mn, tmp)

    def solve(self, A):
        n = len(A)
        mx = []
        mn = []
        ans = []
        for i in range(n):
            if len(mx) == len(mn):
                heappush(mx, -A[i])
                heappush(mn, -heappop(mx))
            else:
                heappush(mn, A[i])
                heappush(mx, -heappop(mn))

            self.find_median(mx, mn, ans)

        return ans


if __name__ == '__main__':
    A = [1, 2, 5, 4, 3]
    B = Solution()
    print(B.solve(A))
