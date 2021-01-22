class Solution:
    def dp(self, A, i, j, dp):
        global ans
        if dp[i][j] != float('inf'):
            return dp[i][j]

        if i == len(A) or j == len(A[i]):
            return float('inf')

        if i == len(A)-1:
            ans = 1
        else:
            ans = min(self.dp(A, i+1, j, dp), self.dp(A, i+1, j+1, dp)) + A[i][j]

        dp[i][j] = ans
        return ans

    def minimumTotal(self, A):
        m = len(A)
        n = len(A[-1])
        dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
        ans = float('inf')
        self.dp(A, 0, 0, dp)
        # for j in range(n):
        #     ans = self.dp(A, 0, j, dp)
        #     break
        return ans

    def solve(self, A):
        m = len(A)
        n = len(A[-1])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[-1][i] = A[-1][i]

        for i in reversed(range(m-1)):
            for j in range(len(A[i])):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + A[i][j]

        return dp[0][0]


if __name__ == '__main__':
    A =     [[2],
           [3, 4],
          [6, 5, 7],
         [4, 1, 8, 3]]

    B = Solution()
    print(B.solve(A))
