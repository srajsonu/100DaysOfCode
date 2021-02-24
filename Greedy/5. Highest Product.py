from heapq import *


class Solution:
    def maxp3(self, A):
        heapify(A)

        p, q, r = nlargest(3, A)
        s, t = nsmallest(2, A)

        return max(p * q * r, s * t * p)


if __name__ == '__main__':
    A = [0, -1, 3, 100, 70, 50]
    B = Solution()
    print(B.maxp3(A))
