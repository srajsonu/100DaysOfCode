class Solution:
    def dp(self, A, i, j, dp):
        global ans
        if dp[i][j]:
            return dp[i][j]

        elif i > j:
            ans = 0

        elif i == j:
            ans = 1

        elif A[i] == A[j]:
            ans = 2 + self.dp(A, i+1, j-1, dp)
        else:
            ans = max(self.dp(A, i+1, j, dp), self.dp(A, i, j-1, dp))

        dp[i][j] = ans
        return ans

    def solve(self, A):
        m = len(A)
        dp = [[0 for _ in range(m)] for _ in range(m)]
        return self.dp(A, 0, m-1, dp)

    def lps(self, A):
        m = len(A)
        dp = [[0 for _ in range(m)] for _ in range(m)]

        for i in range(m):
            dp[i][i] = 1

        for i in reversed(range(m)):
            for j in range(i + 1, m):
                if A[i] == A[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]

if __name__ == '__main__':
    A = "bebeeed"
    B = Solution()
    print(B.solve(A))
    print(B.lps(A))
