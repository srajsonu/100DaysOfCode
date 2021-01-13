import sys
sys.setrecursionlimit(10 ** 9)

class Solution:
    def dp(self, A, i, j, dp):
        m, n = len(A), len(A[0])
        global ans
        if dp[i][j] != float('inf'):
            return dp[i][j]

        if i == m or j == n:
            ans = float('inf')
        elif i == m-1 and j == n-1:
            ans = 1 - A[i][j] if A[i][j] <= 0 else 1
        else:
            ans = min(self.dp(A, i+1, j, dp), self.dp(A, i, j+1, dp)) - A[i][j]

        dp[i][j] = 1 if ans <= 0 else ans
        return dp[i][j]

    def calculateMinimumHP(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
        return self.dp(A, 0, 0, dp)

    def solve(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
        dp[m][n-1] = 1
        dp[m-1][n] = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                ans = min(dp[i+1][j], dp[i][j+1]) - A[i][j]
                dp[i][j] = 1 if ans <= 0 else ans

        return dp[0][0]


if __name__ == '__main__':
    A = [[-2, -3, 3],
         [-5, -10, 1],
         [10, 30, -5]]

    B = Solution()
    print(B.calculateMinimumHP(A))
    print(B.solve(A))
