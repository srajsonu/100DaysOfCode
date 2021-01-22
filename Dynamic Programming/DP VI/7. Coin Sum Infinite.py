import sys
sys.setrecursionlimit(10 ** 9)

class Solution:
    def dp(self, A, B, i, dp):
        mod = 10 ** 6 + 7
        global ans
        if B < 0 or i == len(A):
            return 0

        if dp[i][B] != -1: return dp[i][B]

        if B == 0:
            ans = 1
        else:
            take = self.dp(A, B - A[i], i, dp)
            dont = self.dp(A, B, i+1, dp)
            ans = take + dont
            ans %= mod

        dp[i][B] = ans
        return ans

    def coinchange2(self, A, B):
        m = len(A)
        dp = [[-1 for _ in range(B+1)] for _ in range(m+1)]
        return self.dp(A, B, 0, dp)

    def solve(self, A, B):
        mod = 10 ** 6 + 7
        dp = [0 for _ in range(B + 1)]
        dp[0] = 1
        for i in A:
            for j in range(i, B+1):
                if i <= j:
                    dp[j] += dp[j-i]
                    dp[j] %= mod

        return dp[-1]


if __name__ == '__main__':
    A = [2, 5, 3, 6]
    B = 10
    C = Solution()
    print(C.coinchange2(A, B))
    print(C.solve(A, B))
