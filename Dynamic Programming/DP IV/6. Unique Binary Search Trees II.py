import sys
sys.setrecursionlimit(10 ** 9)

class Solution:
    def dp(self, A, dp):
        if dp[A] != -1:
            return dp[A]
        ans = 0
        if A <= 1:
            ans = 1
        else:
            for i in range(1, A+1):
                ans += self.dp(i-1, dp) * self.dp(A-i, dp)

        dp[A] = ans
        return ans

    def numTrees(self, A):
        dp = [-1 for _ in range(A+1)]
        return self.dp(A, dp)

    def solve(self, A):
        dp = [0 for _ in range(A + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, A+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]

        return dp[-1]

    def catalan(self, A): # Formulae: for nth term = (1/n+1) * (2n C n)
        ans = 1
        for i in range(A):
            ans *= (2 * A - i)
            ans //= (i+1)
        return ans // (A+1)

if __name__ == '__main__':
    A = 3
    B = Solution()
    print(B.numTrees(A))
    print(B.solve(A))
    print(B.catalan(A))
