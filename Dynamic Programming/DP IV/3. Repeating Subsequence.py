import sys
sys.setrecursionlimit(10 ** 9)


class Solution:
    def dp(self, A, B, i, j, dp):
        global ans
        if dp[i][j] != -1:
            return dp[i][j]
        if i == 0 or j == 0:
            if A[i] == B[j] and i != j:
                ans = 1
            else:
                ans = 0
        elif A[i] == B[j] and i != j:
            ans = 1 + self.dp(A, B, i - 1, j - 1, dp)
        else:
            ans = max(self.dp(A, B, i - 1, j, dp), self.dp(A, B, i, j - 1, dp))

        dp[i][j] = ans
        return ans

    def anytwo(self, A):
        n = len(A)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        ans = self.dp(A, A, n - 1, n - 1, dp)
        if ans < 2:
            return 0
        return 1

    def solve(self, A):
        n = len(A)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    dp[i][j] = 1

                if A[i-1] == A[j-1] and i-1 != j-1:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return 1 if dp[-1][-1] >= 2 else 0


if __name__ == '__main__':
    A = "aabb"
    B = Solution()
    print(B.anytwo(A))
    print(B.solve(A))
