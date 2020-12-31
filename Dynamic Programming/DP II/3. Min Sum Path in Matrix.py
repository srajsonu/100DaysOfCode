class Solution:
    def dp(self, A, i, j, dp):
        global ans
        if dp[i][j]:
            return dp[i][j]
        if i == 0 and j == 0:
            return A[i][j]

        elif i == 0 or j == 0:
            if i == 0:
                ans = self.dp(A, i, j-1, dp) + A[i][j]
            else:
                ans = self.dp(A, i-1, j, dp) + A[i][j]
        else:
            x = self.dp(A, i-1, j, dp)
            y = self.dp(A, i, j-1, dp)
            ans = min(x, y) + A[i][j]

        dp[i][j] = ans
        return ans

    def minPathSum(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        return self.dp(A, m-1, n-1, dp)

    def solve(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = A[0][0]

        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + A[i][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + A[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + A[i][j]

        return dp[-1][-1]


if __name__ == '__main__':
    A = [[1, 3, 2],
         [4, 3, 1],
         [5, 6, 1]]

    B = Solution()
    print(B.minPathSum(A))
    print(B.solve(A))
