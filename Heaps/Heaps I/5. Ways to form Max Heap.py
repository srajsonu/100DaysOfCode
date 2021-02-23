from math import log2, factorial


class Solution:
    def ncr(self, n, r):
        return factorial(n) // (factorial(r) * factorial(n - r))

    def ways(self, n, dp):
        mod = 10 ** 9 + 7
        global ans
        if n == 0:
            return 0

        if dp[n] != -1:
            return dp[n]

        if n <= 2:
            ans = 1
        else:
            h = int(log2(n))
            x = (2 ** h) - 1
            l = (x - 1) // 2 + min(n - x, (x + 1) // 2)
            r = n - 1 - l
            ans = self.ncr(n - 1, l) * self.ways(l, dp) * self.ways(r, dp)
            ans %= mod

        dp[n] = ans
        return ans

    def solve(self, A):
        dp = [-1 for _ in range(A + 1)]
        return self.ways(A, dp)


if __name__ == '__main__':
    A = 4
    B = Solution()
    print(B.solve(A))
