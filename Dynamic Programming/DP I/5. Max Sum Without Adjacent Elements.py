class Solution:
    def dp(self, A, i, dp):
        if dp[i]:
            return dp[i]
        if i == 0:
            return A[i]
        if i == 1:
            return max(A[0], A[1])

        x = self.dp(A, i-1, dp)
        y = self.dp(A, i-2, dp)
        ans = max(x, y + A[i])
        dp[i] = ans
        return ans

    def solve(self, A):
        A = [max(A[i][j], A[i+1][j]) for i in range(len(A)-1) for j in range(len(A[0]))]
        n = len(A)
        dp = [0 for _ in range(n+1)]
        return self.dp(A, n-1, dp)

    def adjacent(self, A):
        A = [max(A[i][j], A[i + 1][j]) for i in range(len(A) - 1) for j in range(len(A[0]))]
        n = len(A)
        dp = [0 for _ in range(n)]
        dp[0] = A[0]

        for i in range(1, n):
            dp[i] = max(dp[i-1], dp[i-2] + A[i])

        return dp[-1]

if __name__ == '__main__':
    A = [[74, 37, 82, 1],
        [66, 38, 16, 1]]
    B = Solution()
    print(B.solve(A))
    print(B.adjacent(A))
