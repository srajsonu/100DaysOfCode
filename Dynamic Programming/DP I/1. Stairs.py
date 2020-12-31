class Solution:
    def dp(self, n, dp):
        global ans
        if dp[n]:
            return dp[n]
        if n <= 2:
            ans = n
        else:
            ans = self.dp(n-1, dp) + self.dp(n-2, dp)

        dp[n] = ans
        return ans

    def climbStairs(self, A):
        dp = [0 for _ in range(A+1)]
        return self.dp(A, dp)

if __name__ == '__main__':
    A = 3
    B = Solution()
    print(B.climbStairs(A))
