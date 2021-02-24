from heapq import *


class Solution:
    def mice(self, A, B):
        heapify(A)
        heapify(B)
        ans = []

        while A and B:
            x = heappop(A)
            y = heappop(B)

            ans.append(abs(x-y))

        return max(ans)



if __name__ == '__main__':
    A = [-4, 2, 3]
    B = [0, -2, 4]
    C = Solution()
    print(C.mice(A, B))
