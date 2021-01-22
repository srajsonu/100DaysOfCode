class Solution:
    def dp(self, A, B, dp):
        mod = 10 ** 9 + 7

        if B < 0: return 0
        if A == 0 and B == 0: return 1
        if A == 0: return 0

        if dp[A][B] != -1:
            return dp[A][B]

        ans = 0
        for i in range(10):
            ans += self.dp(A - 1, B - i, dp)
            ans %= mod

        dp[A][B] = ans
        return ans

    def solve(self, A, B):
        mod = 10 ** 9 + 7
        dp = [[-1] * (B + 1) for _ in range(A + 1)]
        ans = 0
        for i in range(1, 10):
            ans += self.dp(A - 1, B - i, dp)
            ans %= mod
        return ans

if __name__ == '__main__':
    A = 3
    B = 4
    C = Solution()
    print(C.solve(A, B))
