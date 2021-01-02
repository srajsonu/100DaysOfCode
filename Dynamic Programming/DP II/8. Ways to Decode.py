import sys
sys.setrecursionlimit(10 ** 9)
class Solution:
    def dp(self, A, i, dp):
        if dp[i]:
            return dp[i]
        if i == len(A):
            return 1

        if A[i] == '0':
            return 0

        w1 = self.dp(A, i+1, dp)
        w2 = 0
        if i < len(A) - 1 and int(A[i:i+2]) <= 26 and int(A[i:i+2]) > 0:
            w2 = self.dp(A, i+2, dp)

        dp[i] = w1 + w2
        return w1 + w2

    def numDecodings(self, A):
        n = len(A)
        dp = [0 for _ in range(n+1)]
        return self.dp(A, 0, dp)

if __name__ == '__main__':
    A = "12"
    B = Solution()
    print(B.numDecodings(A))
