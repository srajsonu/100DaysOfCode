from heapq import heapify, heappop, heappush


class Solution:
    def solve(self, A):
        heapify(A)

        ans = 0
        while len(A) > 1:
            tmp1 = heappop(A)
            tmp2 = heappop(A)
            tmp3 = (tmp1 + tmp2)
            ans += tmp3
            heappush(A, tmp3)

        return ans

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = Solution()
    print(B.solve(A))
