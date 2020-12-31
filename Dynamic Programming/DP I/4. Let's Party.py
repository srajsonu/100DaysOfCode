import sys

sys.setrecursionlimit(10 ** 9)


# Top-Down
class Solution:
    def dp(self, n, dp):
        global ans
        if dp[n]:
            return dp[n]

        if n <= 2:
            ans = n
        elif n == 3:
            ans = 4
        else:
            ans = self.dp(n - 1, dp) + (n - 1) * self.dp(n - 2, dp)
            ans %= 10003

        dp[n] = ans
        return ans

    def party(self, A):
        dp = [0 for _ in range(A + 1)]
        return self.dp(A, dp)

    # Bottom-Up
    def solve(self, A):
        if A <= 2:
            return A
        if A == 3:
            return 4
        dp = [0 for _ in range(A + 1)]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        for i in range(4, A + 1):
            dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]
            dp[i] %= 10003

        return dp[-1]


if __name__ == '__main__':
    A = 500
    B = Solution()
    print(B.party(A))
    print(B.solve(A))
