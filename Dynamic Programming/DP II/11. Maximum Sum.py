class Solution:
    def dp(self, A, i, j, dp):
        ans = float('-inf')
        print(i, j)
        if dp[i][j] != float('-inf'):
            return dp[i][j]

        elif i == 0 or j == 0 or  j == 1 or  j == 2:
            if i == 0 and j == 0:
                ans = A[i] * B
            elif j == 1:
                ans = self.dp(A, i, j-1, dp) +  A[i] * self.C
            elif j == 2:
                ans = self.dp(A, i, j-1, dp)  + A[i] * self.D
        # elif j == 1:
        #     ans = self.dp(A, i, j-1, dp)
        # elif j == 2:
        #     ans = self.dp(A, i, j-1, dp)
        else:
            x = max(self.dp(A, i-1, 0, dp), A[i] * self.B)
            y = max(self.dp(A, i-1, 1, dp), x + A[i] * self.C)
            z = max(self.dp(A, i-1, 2, dp), y + A[i] * self.D)
            ans = z

        dp[i][j] = ans
        return ans

    def maxSum(self, A, B, C, D):
        self.B = B
        self.C = C
        self.D = D
        n = len(A)
        dp = [[float('-inf') for _ in range(3)] for _ in range(n)]
        return self.dp(A, n-1, 0, dp), dp

    def solve(self, A, B, C, D):
        n = len(A)
        dp = [[float('-inf') for _ in range(3)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = max(dp[i-1][0], A[i] * B)
            dp[i][1] = max(dp[i-1][1], dp[i][0] + A[i] * C)
            dp[i][2] = max(dp[i-1][2], dp[i][1] + A[i] * D)

        return dp[-1][-1]

if __name__ == '__main__':
    A = [1, 5, -3, 4, -2]
    B = 2
    C = 1
    D = -1
    E = Solution()
    print(E.maxSum(A, B, C, D))
    #print(E.solve(A, B, C, D))
