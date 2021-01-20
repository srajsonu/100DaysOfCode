class Solution:
    def dp(self, A, i, dp):
        global ans
        if dp[i]:
            return dp[i]
        if i == 0:
            ans = 1
        else:
            take = 1 + self.dp(A, i-1, dp)
            dont = self.dp(A, i-1, dp)
            ans = take + dont

        dp[i] = ans
        return ans

    def solve(self, A):
        n = len(A)
        dp = [0 for _ in range(n)]
        return self.dp(A, n-1, dp)

if __name__ == '__main__':
    A = 'aba'
    B = Solution()
    print(B.solve(A))
