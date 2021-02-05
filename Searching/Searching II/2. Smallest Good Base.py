from math import log2


class Solution:
    def solve(self, A):
        n = int(A)
        m = int(log2(n)) + 1

        for i in range(m, 0, -1):
            l = 2
            h = n - 1
            while l <= h:
                k = (l+h) // 2
                sm = (k ** i - 1) // (k-1)
                if sm == n:
                    return k
                if sm > n:
                    h = k - 1
                else:
                    l = k + 1

        return -1

if __name__ == '__main__':
    A = "6"
    B = Solution()
    print(B.solve(A))
