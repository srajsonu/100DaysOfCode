class Solution:
    def dp(self, A, i, dp):
        if dp[i]:
            return dp[i]

        if i >= len(A)-1:
            return 0

        ans = float('inf')
        max_steps = A[i]

        while max_steps:
            ans = min(ans, 1 + self.dp(A, i + max_steps, dp))
            max_steps -= 1

        dp[i] = ans
        return ans

    def jump(self, A):
        n = len(A)
        dp = [0 for _ in range(n+1)]
        return self.dp(A, 0, dp)

    def solve(self, A):
        n = len(A)
        dp = [float('inf') for _ in range(n)]
        dp[n-1] = 0

        for i in range(n-2, -1, -1):
            for j in range(1, A[i]+1):
                if i + j < n:
                    dp[i] = min(dp[i], 1 + dp[j])

        return dp

if __name__ == '__main__':
    A = [2,3,1,1,4]
    B = Solution()
    print(B.jump(A))
    print(B.solve(A))
