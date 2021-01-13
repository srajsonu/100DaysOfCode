import sys
sys.setrecursionlimit(10 ** 9)
class Solution:
    def dp(self, A, dp):
        mod = 10003
        global ans
        if dp[A]:
            return dp[A]
        elif A <= 2:
            ans = A
        else:
            ans = self.dp(A-1, dp) + (A-1) * self.dp(A-2, dp)
            ans %= mod

        dp[A] = ans
        return ans

    def solve(self, A):
        dp = [0 for _ in range(A+1)]
        return self.dp(A, dp)

    def isParty(self, A):
        dp = [0 for _ in range(A+1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, A+1):
            dp[i] = dp[i-1] + (i-1) * dp[i-2]

        return dp[-1]

if __name__ == '__main__':
    A = 3
    B = Solution()
    print(B.solve(A))
    print(B.isParty(A))
