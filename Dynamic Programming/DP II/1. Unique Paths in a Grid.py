import sys
sys.setrecursionlimit(10 ** 9)

#Top-Down
class Solution:
    def dp(self, A, i, j, dp):
        global ans
        if dp[i][j]:
            return dp[i][j]

        if A[i][j] == 1:
            return 0

        if A[0][0] == 1 or A[-1][-1] == 1:
            return 0

        if i == 0 and j == 0:
            dp[i][j] = 1
            return 1

        if i == 0 or j == 0 and A[i][j] != 1:
            if i == 0:
                ans = self.dp(A, i, j-1, dp)
            if j == 0:
                ans = self.dp(A, i-1, j, dp)

        elif A[i][j] == 0:
            ans = self.dp(A, i-1, j, dp) + self.dp(A, i, j-1, dp)

        dp[i][j] = ans
        return ans

    def uniquePathsWithObstacles(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[0]*(n) for _ in range(m)]
        self.dp(A, m-1, n-1, dp)
        return dp[-1][-1]

#Bottom-Up
    def solve(self, A):
        if A[0][0] == 1 or A[-1][-1] == 1:
            return 0
        m = len(A)
        n = len(A[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            if A[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(m):
            if A[i][0] == 1:
                break
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if A[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]



if __name__ == '__main__':
    A = [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]]

    C = [ [0, 0],
          [0, 0],
          [0, 0],
          [1, 0],
          [0, 0]]

    B = Solution()
    print(B.uniquePathsWithObstacles(C))
    print(B.solve(C))
